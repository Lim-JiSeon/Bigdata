import os
import sys
import urllib.request
import json
import kss
from kss import split_sentences
import pandas as pd
import numpy as np
import re
from hanspell import spell_checker
from kiwipiepy import Kiwi

### py-hanspell 설치 오류 해결 및 실행 방법
# git clone https://github.com/ssut/py-hanspell
# cd py-hanspell
# python setup.py install
# result = spell_checker.check(u'안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다.')
# print(result.checked)

df = pd.read_excel('C:/Users/ksc/Desktop/F4301_T4400.xlsx')
# print(df['조리법'])


# 조리법 칼럼에서 특수문자 제거
df['조리법'] = df['조리법'].str.replace(pat=r'[^\w\s.]', repl=r'', regex=True)
df['조리법'] = df['조리법'].str.replace(pat=r'[a-zA-Z]+', repl= r'', regex=True)
# df['조리법'] = df['조리법'].str.replace(r"[a-zA-Z]", "")
# new_str = re.sub(r"[a-zA-Z]", "", str(df['조리법']))
# df['조리법'] = new_str

print(df['조리법'])
recipe = df["조리법"]

df = df.dropna(axis=0)

# 맞춤법 교정
# result = spell_checker.check(recipe[3995])
# print(result)
# df['조리법_맞춤법'] = spell_checker.check(str(df['조리법']))
# print(df['조리법'])
# print(df['조리법_맞춤법'])




# 문장 분리(띄어쓰기) 및 맞춤법 교정
kiwi = Kiwi()

# res = kiwi.split_into_sents(df['조리법'][0])
# print(res)
# res1 = ""
# for i in range(0, len(res)):
#     res1 = res1 + str(res[i].text) + '\n'
# print(res1)


# hanspell 이용하여 맞춤법 교정
df["조리법_spell"] = 0
df['조리법_맞춤법'] = 0

# sentence = kiwi.split_into_sents(df['조리법'][1])
# res =spell_checker.check(sentence[3])
# print(res.checked)

for i in range(0, len(df['조리법'])):
    sentence = kiwi.split_into_sents(df['조리법'][i])
    for j in range(0, len(sentence)):
        sentence_res = spell_checker.check(str(sentence[j].text))
        df['조리법_spell'][i] = str(df['조리법_spell'][i]) + str(sentence_res.checked) + "\n"
    # check1 = spell_checker.check(str(df['조리법_spell'][i]))
    # df['조리법_맞춤법'] = check1.checked

# print(df['조리법_spell'])

# print(df['조리법_spell'])
df.to_csv('C:/Users/ksc/Desktop/음식레시피_전처리/조리법_교정.csv', encoding='utf-8', index = None)
# df.to_excel("C:/Users/ksc/Desktop/음식레시피_전처리/조리법_교정.xlsx", encoding = 'utf-8')




