import os
import sys
import urllib.request
import json
import kss
from kss import split_sentences
import pandas as pd
import numpy as np
import re
from googletrans import Translator
translator = Translator()

df = pd.read_excel('F4301_T4400.xlsx')
df["recipe_eng"] = 0
df["recipe_kor"] = 0

df['조리법'] = [re.sub('[^A-Za-z0-9가-힣. ]', '', str(s)) for s in df['조리법']]
recipe = df['조리법']

df = df.dropna()

## googletrans 이용

for i in range(0, len(recipe)):
  try:
  # for j in range(0, len(recipe[i])):
    # print(recipe[i][j])
    en = translator.translate(str(recipe[i]), src="ko", dest="en")
    print(en.text)
    # print(en.text)
    # ko = translator.translate(str(en.text), src="en", dest="ko")
    # recipe[i][j] = ko.text
  # print(recipe[i])
    df["recipe_eng"].iloc[i] = en
  except:
    df["recipe_eng"].iloc[i] = "조리법 없음"

for i in range(0, len(recipe)):
  try:
    ko = translator.translate(recipe[i], src="en", dest="ko")
    print(ko.text)
    df["recipe_kor"].iloc[i] = ko
  except:
    df["recipe_kor"].iloc[i] = "조리법 없음"

df.to_excel("레시피_전처리.xlsx", encoding = 'utf-8')



