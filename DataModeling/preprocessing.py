# -*- coding: cp949 -*-

from collections import Counter
import numpy as np
import ast, os
import utils

def process1():
    print('재료 단위 제거')
    #N = utils.Normalize()

    fp, fn = utils.filePaths(2)
    for p, n in zip(fp, fn): 
        data = utils.readFile(p, n, 2).values.tolist()
        
        # filter
        subDt = []
        for d in data:
            minT = d[4].find('분')
            if minT != -1 and int(d[4][ : minT]) <= 30 and d[5] in ['아무나', '초급']:   # 30분 이내 + 아무나, 초급 난이도
                if d[3] != 'X' and int(d[3].replace('인분', '')) <= 3:                   # 3인분 이내
                    subDt.append(d)

        df = utils.makeDf(subDt, ['Key', '메인사진', '요리명', '인분', '소요시간', '난이도', '재료', '조리법', '조리사진'])
        utils.saveFile(os.getcwd(), f'1_{n}', df, 2)

        subDt = np.array(subDt)

        ingred = np.transpose(subDt[ : , 6 : 7]).tolist()[0]
        ingred_dict = []
        for i in ingred:
            try:
                ingred_dict.append(ast.literal_eval(i))
            except:
                continue

        ingreds = []
        for i in ingred_dict:
            ingreds.append(i[1])

        # normalize 진행시
        '''
        for i in ingred_dict:
            for j in i:
                ingred = N.process(' '.join(j)).split()
                ingreds.append(''.join(ingred))
        '''

        counts = Counter(ingreds)

        counts_key = list(counts.keys())
        counts_val = list(counts.values())

        param = []
        for i in range(len(counts_key)):
            param.append([counts_key[i], counts_val[i]])  
    
        df = utils.makeDf(param, ['재료', '빈도수'])
        utils.saveFile(os.getcwd(), f'2_{n}', df, 2)


def process2():
    fp, fn = utils.filePaths(2)

    for p, n in zip(fp, fn): 
        data = utils.readFile(p, n, 2).values.tolist()

        ingreds = []
        counts = []
        for d in data:
            d = np.array(d).transpose().tolist()

            # 재료명의 공백 제거
            #for i in range(len(d[0])):
            #    d[0][i] = d[0][i].replace(' ', '')

            i = d[1]
            c = d[2]
            if i in ingreds:
                idx = ingreds.index(i)
                counts[idx] += int(c)
            else:
                ingreds.append(i)
                counts.append(int(c))

        newData = []
        for i in range(len(ingreds)):
            newData.append([ingreds[i], counts[i]])
        newData = sorted(newData, key=lambda x: x[1], reverse=True)

    df = utils.makeDf(df, ['재료', '빈도수'])
    utils.saveFile(os.getcwd(), '재료사전', df, 2)

print('1. 소요시간, 난이도 필터링 및 재료 빈도수')
print('2. 재료 빈도수 취합')
print('선택 :', end = ' ')
n = int(input())

if n == 1:
    process1()
elif n == 2:
    process2()