# -*- coding: utf-8 -*-

import os
import sys
import urllib.request
import json
import kss
from kss import split_sentences
import pandas as pd
import numpy as np
import re
#from hanspell import spell_checker
from kiwipiepy import Kiwi

'''
kiwi = Kiwi()

def process(recipe):
    lines = kiwi.split_into_sents(recipe)

    newLines = []
    for line in lines:
        res = line[0].text[ : 3] + re.sub('[^ㄱ-ㅎ가-힣a-zA-Z0-9\s]', '', line[0].text[3 : ])
        newLines.append(res)

    return newLines
'''

df = pd.read_excel('F4301_T4400.xlsx')
# print(df['조리법'])

# def remove_numeric_prefix(string):
#     # 숫자 선행문자를 제거합니다.
#     result = re.sub(r'^\d+\.\s*', '', string)
#     return result

def remove_prefix_before_numeric(string):
    # 숫자와 점으로 시작하는 선행문자 앞의 문자열을 제거하고 숫자와 점은 남김
    result = re.sub(r'.*?(\d+\.\s*)', r'\1', string)
    return result

def add_numbers(string):
    # 문장의 순서를 위해 숫자를 추가하고 선행문자를 제거
    lines = string.strip().split('\n')
    result = ""
    for i, line in enumerate(lines, start=1):
        line = re.sub(r'^\d+\.', str(i) + '.', line.strip())
        result += line + '\n'
    return result

def fill_missing_numbers(string):
    # 문자열 앞 부분을 비교하여 'tip)'이 존재하면 숫자를 채우지 않고 pass.
    lines = string.strip().split('\n')
    result = ""
    last_number = 0
    for line in lines:
        if re.search(r'^tip\)', line):
            result += line + '\n'
        else:
            match = re.match(r'^(\d+)\.', line)
            if match:
                number = int(match.group(1))
                if number == last_number + 1:
                    last_number = number
                    result += line + '\n'
                else:
                    result += f"{last_number + 1}. {line[match.end():].strip()}\n"
                    last_number += 1
            else:
                result += line + '\n'
    return result

def replace_numbers(string):
    # 문장의 숫자를 차례대로 변경하여 출력
    lines = string.strip().split('\n')
    result = ""
    count = 1
    for line in lines:
        if re.match(r'^\d+\.', line):
            line = re.sub(r'^\d+', str(count), line)
            count += 1
        result += line + '\n'
    return result

def add_tip(string):
    # 숫자와 마침표가 없는 문장 앞에 "tip)"을 추가하여 출력
    lines = string.strip().split('\n')
    result = ""
    for line in lines:
        if not line.startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.')):
            line = "tip) " + line
        result += line + '\n'
    return result

def rearrange_string(string):
    # 숫자와 '.'을 기준으로 문자열을 분할하여 줄을 바꿔줌
    lines = re.findall(r'(\d+\.\s*.*?)(?=\d+\.|$)', string, re.DOTALL)
    result = '\n'.join(lines)
    return result

def remove_trailing_chars(string):
    # 문자열에서 문자 또는 숫자 또는 "."이 나올 때까지 오른쪽 끝 부분 문자열 제거
    pattern = r"[^A-Za-z0-9.]"
    match = re.search(pattern, string)
    if match:
        index = match.start()
        result = string[:index]
    else:
        result = string
    return result



# 조리법 칼럼에서 특수문자 제거
df['조리법'] = df['조리법'].str.replace(pat=r'[^\w\s/~,.()\n%:]', repl=r'', regex=True)
df['조리법'] = df['조리법'].str.replace('n', '', regex=True)
# df['조리법'] = df['조리법'].str.replace(pat=r'[a-zA-Z^cmlkg]+', repl= r'', regex=True)
# df['조리법'] = df['조리법'].str.replace(r"[a-zA-Z]", "")
# new_str = re.sub(r"[a-zA-Z]", "", str(df['조리법']))
# df['조리법'] = new_str

print(df['조리법'])
recipe = df["조리법"]

df = df.dropna(axis=0)


# 문장 분리
kiwi = Kiwi()

# res = kiwi.split_into_sents(df['조리법'][0])
# print(res)
# res1 = ""
# for i in range(0, len(res)):
#     res1 = res1 + str(res[i].text) + '\n'
# print(res1)

df["조리법_spell"] = 0


for i in range(0, len(df['조리법'])):
    sentence = kiwi.split_into_sents(df['조리법'][i])
    # print(sentence)
    for j in range(0, len(sentence)):
        # print(sentence[j].text)
        # res = str(sentence[j].text).lstrip('[^0-9]')   # 문장 나눠졌을 때 한 문장 당 숫자 선행문자 제거
        # res = str(res).lstrip('[^\w]')

        # res = remove_prefix_before_numeric(str(sentence[j].text))
        df['조리법_spell'][i] = str(df['조리법_spell'][i]) + str(sentence[j].text) + "\n"
    df['조리법_spell'][i] = add_numbers(str(df['조리법_spell'][i]))
    df['조리법_spell'][i] = add_tip(str(df['조리법_spell'][i]))
    df['조리법_spell'][i] = rearrange_string(str(df['조리법_spell'][i]))
    df['조리법_spell'][i] = fill_missing_numbers(str(df['조리법_spell'][i]))
    df['조리법_spell'][i] = replace_numbers(str(df['조리법_spell'][i]))
    df['조리법_spell'][i] = rearrange_string(str(df['조리법_spell'][i]))
    # df['조리법_spell'][i] = remove_trailing_chars(str(df['조리법_spell'][i]))
df['조리법_spell'] = df['조리법_spell'].replace(",\n","", regex=True)
df['조리법_spell'] = df['조리법_spell'].replace("xa0","", regex=True)
# df['조리법_spell'] = df['조리법_spell'].replace("\n\n","\n", regex=True)
# df['조리법_spell'] = add_numbers(str(df['조리법_spell']))
print(df['조리법_spell'])


df.to_csv('조리법_교정(kiwi)ver10.csv', encoding='utf-8', index = None)






'''
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
'''