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

# df = pd.read_excel('F4301_T4400.xlsx')
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

def space_tip(result):
    # 첫 번째 "tip)"의 위치를 찾습니다
    first_index = result.find("tip)")

    # 두 번째 "tip)"의 위치를 찾습니다
    second_index = result.find("tip)", first_index + 1)

    # 두 번째 "tip)"을 "\ntip)"로 변경합니다
    if second_index != -1:
        result = result[:second_index] + "\n" + result[second_index:]

    print(result)



# 조리법 칼럼에서 특수문자 제거
def clean_recipe_text(recipe_list):
    # cleaned_list = []
    cleaned_text = ' '.join(map(str, recipe_list))
    cleaned_text = cleaned_text.replace(r'[^\w\s.]', r'')
    cleaned_text = cleaned_text.replace(r'[a-zA-Z]+', r'')
    # for text in recipe_list:
    #     cleaned_text = re.sub(r'[^\w\s/~,.()\n%:]', '', text)
    #     cleaned_text = cleaned_text.replace('n', '')
        # cleaned_list.append(cleaned_text)
    return cleaned_text

# df = df.dropna(axis=0)


# 문장 분리
def preprocess_recipe_text(recipe_text):
    kiwi = Kiwi()
    sentence_list = kiwi.split_into_sents(recipe_text)
    processed_recipe = ""

    for sentence in sentence_list:
        processed_recipe += sentence.text + "\n"
    processed_recipe = add_numbers(processed_recipe)
    processed_recipe = add_tip(processed_recipe)
    processed_recipe = rearrange_string(processed_recipe)
    processed_recipe = fill_missing_numbers(processed_recipe)
    processed_recipe = replace_numbers(processed_recipe)
    processed_recipe = rearrange_string(processed_recipe)

    processed_recipe = processed_recipe.replace(",\n", "")
    processed_recipe = processed_recipe.replace("xa0", "")
    # processed_recipe = processed_recipe.replace("tip) (\ntip)", "tip)")
    # processed_recipe = space_tip(processed_recipe)

    return processed_recipe


recipe_list = ['1. 양념장을 먼저 만들어 준비해 주세요 \n고추장2스푼 고춧가루2스푼 \n간장2스푼 설탕1스푼 매실청2스푼\n다진마늘1스푼 후춧가루 톡톡톡톡\n고루 잘 섞어 주세요매실청 없으신 분은 맛술 대체하세요 ', '2. 달궈진 후라이팬에 기름을 살짝 두르고 고기를 올려주세요 ', '3. 고기가 반 정도 익을 때 까지 볶아준뒤 중불 ', '4. 잘라놓은 대파 2대중 1대를 고기위로 넣고 같이 볶아 주세요 중불 ', '5. 파와 고기가 잘 섞여 반쯤 익어있던 고기가 다 익으면 양파를 넣어주세요 중불 ', '6. 양파를 넣은뒤 곧바로 양념장을 넣고 잘 섞어가며 볶아줍니다 중불 ', '7. 양념장이 고기와 잘 섞여지면 중약불 ', '8. 굴소스 1스푼과 중약불 ', '9. 남아있던 대파1대 청양고추를 넣고 중불 ', '10. 마지막으로 고루 섞어가며 휘리릭 볶아주면 제육볶음 완성입니다^^ 중불 ']
cleaned_recipe_text = clean_recipe_text(recipe_list)
# print(cleaned_recipe_text)
processed_recipe = preprocess_recipe_text(cleaned_recipe_text)
print(processed_recipe)


# df.to_csv('조리법_교정(kiwi)ver10.csv', encoding='utf-8', index = None)






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