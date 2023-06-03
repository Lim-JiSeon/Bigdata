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
                if d[3] != 'X' and int(d[3][0]) <= 3:                   # 3인분 이내
                    subDt.append(d)

        utils.saveFile(os.getcwd(), f'1_{n}', subDt, 2, ['Key', '메인사진', '요리명', '인분', '소요시간', '난이도', '재료', '조리법', '조리사진'])

        opt = 0
        if opt == 1:    # 필터링 적용
            subDt = np.array(subDt)
        else:           # 필터링 미적용
            subDt = np.array(data)
        ingred = np.transpose(subDt[ : , 6 : 7]).tolist()[0]
        ingred_dict = []
        for i in ingred:
            try:
                ingred_dict.append(ast.literal_eval(i))
            except:
                continue

        ingreds = []
        conds = []
        for ingr in ingred_dict:
            for i in ingr:
                if i == []:
                    continue
                attr = i[0]
                if attr == '재료':
                    ingreds.append(i[1])
                elif attr == '양념':
                    conds.append(i[1])

        # normalize 진행시
        '''
        for i in ingred_dict:
            for j in i:
                ingred = N.process(' '.join(j)).split()
                ingreds.append(''.join(ingred))
        '''
        dt = []
        counts = Counter(ingreds)

        counts_key = list(counts.keys())
        counts_val = list(counts.values())
        for i in range(len(counts_key)):
            dt.append([counts_key[i], counts_val[i], '재료'])  

        counts = Counter(conds)

        counts_key = list(counts.keys())
        counts_val = list(counts.values())
        for i in range(len(counts_key)):
            dt.append([counts_key[i], counts_val[i], '양념'])

        dt.sort(key = lambda x : x[1], reverse = True)
        utils.saveFile(os.getcwd(), f'2_{n}', dt, 2, ['재료', '빈도수', '속성'])

def process2():
    ingreds = [[], []]
    counts = [[], []]
    fp, fn = utils.filePaths(2)
    for p, n in zip(fp, fn): 
        data = utils.readFile(p, n, 2).values.tolist()

        for d in data:
            d = np.array(d).transpose().tolist()

            # 재료명의 공백 제거
            #for i in range(len(d[0])):
            #    d[0][i] = d[0][i].replace(' ', '')

            i = d[0]
            c = d[1]
            a = d[2]
            if a == '재료':
                opt = 0
            elif a == '양념':
                opt = 1
            
            if i in ingreds[opt]:
                idx = ingreds[opt].index(i)
                counts[opt][idx] += int(c)
            else:
                ingreds[opt].append(i)
                counts[opt].append(int(c))

    op = False
    newData = []
    if op:          # 양념 취급 받았던 재료 양념으로 넘기기
        for o, a in enumerate(['재료', '양념']):
            for i, c in zip(ingreds[o], counts[o]):
                newData.append([i, c, a])
    else:         
        for i, c in zip(ingreds[0], counts[0]):
            if i in ingreds[1]:
                idx = ingreds[1].index(i)
                if c <= counts[1][idx]:
                    newData.append([i, c + counts[1][idx], '양념'])
                else:
                    newData.append([i, c + counts[1][idx], '재료'])
            else:
                newData.append([i, c, '재료'])
        for i, c in zip(ingreds[1], counts[1]):
            if i not in ingreds[0]:
                newData.append([i, c, '양념'])

    newData = sorted(newData, key = lambda x: x[1], reverse=True)
    utils.saveFile(os.getcwd(), '재료사전.xlsx', newData, 2, ['재료', '빈도수', '속성'])

print('1. 소요시간, 난이도 필터링 및 재료 빈도수')
print('2. 재료 빈도수 취합')
print('선택 :', end = ' ')
n = int(input())

if n == 1:
    process1()
elif n == 2:
    process2()