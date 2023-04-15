# -*- coding: cp949 -*-

from collections import Counter
import pandas as pd
import numpy as np
from tkinter import filedialog
import ast
import os
import re

def fileOpen():
    global fileName
    fileName = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("*.xlsx","*xlsx"), ("*.xls","*xls"), ("*.csv","*csv"), ("all files", "*.*")))

    df = pd.read_excel(fileName)
    dt = df.values.tolist()
    return dt

def fileCreate(dt, val):
    global fileName

    try:
        folder = '10000recipeData'  # 엑셀 저장 폴더명
        os.mkdir(folder)
    except:
        pass

    pattern = r'F\d+_T\d+'
    fName = re.findall(pattern, fileName)[0]

    fName = f'{folder}/{fName}_{val}.xlsx'

    cols = [['Key', '요리명', '인분', '소요시간', '난이도', '재료', '조리법'], ['재료', '빈도수']]
    df = pd.DataFrame(dt, columns = cols[val - 1])

    df.to_excel(fName, index = False)

def process1():
    dt = fileOpen()

    subDt = []
    for i in dt:
        min = i[3].find('분')
        if min != -1 and int(i[3][ : min]) <= 30 and i[4] in ['아무나', '초급']:
            subDt.append(i)

    fileCreate(subDt, 1)
    subDt = np.array(subDt)

    ingred = np.transpose(subDt[ : , 5 : 6]).tolist()[0]
    ingred_dict = []
    for i in ingred:
        temp = ast.literal_eval(i)
        ingred_dict.append(temp)

    ingreds = []
    for i in ingred_dict:
        for j in i:
            ingreds.append(list(j.keys())[0])

    counts = Counter(ingreds)

    counts_key = list(counts.keys())
    counts_val = list(counts.values())

    param = []
    for i in range(len(counts_key)):
        param.append([counts_key[i], counts_val[i]])  
    
    fileCreate(param, 2)

def process2():
    pass

print('1. 소요시간, 난이도 필터링 및 재료 빈도수')
print('2. 재료 빈도수 취합')

n = int(input())

while 1:
    try:
        if n == 1:
            process1()
        if n == 2:
            process2()
    except:
        break