# -*- encoding= cp949 -*-

from konlpy.tag import Komoran
import os, re
import utils

def dishNameExtract(dishNames, ingreds):
    dishNameList = []
    for ingred in ingreds:
        for dishName in dishNames:
            dishName = re.sub('[^a-zA-Z0-9\s\uAC00-\uD7AF]', '', dishName)  # 특수문자 제거
            if ingred in dishName and tagging.pos(dishName)[0][1] == 'NNP':
                dishNameList.append(dishName)
    dishNameList = list(set(dishNameList))
    return dishNameList

def process():
    print('재료사전 선택')
    ingreds_ds = []
    fp, fn = utils.filePaths(2) # 요리사전 파일 읽기
    for p, n in zip(fp, fn): 
        ingreds_df = utils.readFile(p, n, 2)
        ingreds_ds += ingreds_df.values.tolist()
 
    print('\n빈도수 제한 : ', end = '')
    limit = int(input())
    ingreds_ds = [ingreds_ds[i][0] for i in range(len(ingreds_ds)) if ingreds_ds[i][1] >= limit]

    print('\n요리명을 추출할 엑셀파일 선택(여러개 선택 가능)')
    print('필터링된 데이터 선택')

    fp, fn = utils.filePaths(2) # 요리명을 추출할 엑셀파일 열기
    for p, n in zip(fp, fn): 
        recipe_df = utils.readFile(p, n, 2)
        recipe_ds = recipe_df.values.tolist()

        newDs = []
        for recipe in recipe_ds[1:2]:
            dishName = recipe[2].split()

            res = dishNameExtract(dishName, ingreds_ds)
            if res != []:
                newDs.append(recipe)
                newDs[-1][2] = ' '.join(res)
                print(newDs[-1])

        name = n[2 : ]
        utils.saveFile(os.getcwd(), f'3_{name}', newDs, 2, recipe_df.columns)

tagging = Komoran()
process()