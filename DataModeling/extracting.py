# -*- encoding= cp949 -*-

from collections import OrderedDict
import replace_ingred_synonym as syn
import recipe_spell as rs
import os, re, ast
import utils

def process():
    os.system('cls')

    '''
    print('재료사전 선택')
    ingreds_ds = []
    fp, fn = utils.filePaths(2) # 재료사전 파일 읽기
    for p, n in zip(fp, fn): 
        ingreds_df = utils.readFile(p, n, 2)
        ingreds_ds += ingreds_df.values.tolist()

    opt = 2     # 수동, 자동
    if opt == 1:
        print('\n빈도수 제한 : ', end = '')
        limit = int(input())
    else:
        limit = 20
    ingreds_ds = [ingreds_ds[i][0] for i in range(len(ingreds_ds)) if ingreds_ds[i][1] >= limit]
    ingreds_ds += utils.readFile(os.getcwd(), '3. Ingreds.txt')
    '''
    N = utils.useN()
    model = syn.useModel()

    ingr_dict = {}
    type_dict = {}
    print('재료사전 선택')
    fp, fn = utils.filePaths(2)
    for p, n in zip(fp, fn): 
        df = utils.readFile(p, n, 2).values.tolist()
        for l in df:
            ingr_dict[l[1]] = int(l[2])
            type_dict[l[1]] = l[3]

    print('엑셀파일 선택(여러개 선택 가능)')
    print('필터링된 데이터 선택\n')
    fp, fn = utils.filePaths(2) # 요리명을 추출할 엑셀파일 열기
    for p, n in zip(fp, fn): 
        print(n)
        df = utils.readFile(p, n, 2)
        ds = df.values.tolist()

        newDt = []
        for d in ds:
            try:    # 데이터 손실이 일어났을 경우를 대비
                # 요리명
                
                #words = []
                #doc = model(dish)
                #for entity in doc.ents:
                #    if entity.label_ == 'DISH':
                #        words.append(entity.text)

                dish = N.process(d[2], 1)
                if dish == '':
                    continue
                dish = ' '.join(list(OrderedDict.fromkeys(dish.split())))

                # 재료
                if d[6] == '[]':
                    continue
                newIngreds = []
                ingreds = ast.literal_eval(d[6])
                for i in ingreds:
                    sim = syn.replace_similar_words(model, i[1])
                    if sim in ingr_dict and i[1] in ingr_dict:
                        if ingr_dict[sim] > ingr_dict[i[1]]:
                            i[0] = type_dict[sim]
                            i[1] = sim
                    elif sim in ingr_dict:
                        i[0] = type_dict[sim]
                        i[1] = sim                        
                    newIngreds.append(i)

                ingreds = newIngreds

                # 레시피
                if d[7] == '[]':
                    continue
                recipe = ast.literal_eval(d[7])
                recipe = [line for line in rs.process(recipe).split('\n') if line != '']

                if d[8] == '[]':
                    continue
                recipe_pt = ast.literal_eval(d[8])

            except:
                continue
            
            # 모든 데이터가 온전한 경우만 저장
            if not(d[3] == 'X' or d[4] == 'X' or d[5] == 'X'):
                nowDt = [d[0], d[1], dish, d[3], d[4], d[5], ingreds, recipe, recipe_pt]
                #print(nowDt)
                #print('===================================================================================================')
                newDt.append(nowDt)

        name = n[2 : ]
        utils.saveFile(os.getcwd(), f'3_{name}', newDt, 2, df.columns)

process()