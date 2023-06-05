import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer

df = pd.read_excel('조리법_필터링_종합2.xlsx')

sample_index = 11
sample_title = df['조리법'][sample_index]
print(sample_title)

sample_content = df['조리법'][sample_index]
print(sample_content)

def preprocessing(text):
    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)
    # 특수문자 제거
    # text = re.sub('[?.,;:|\)*~`’!^\-_+<>@\#$%&-=#}※]', '', text)
    # 한글, 영문, 숫자만 남기고 모두 제거
    # text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z0-9]', ' ', text)
    # 한글, 영문만 남기고 모두 제거.
    text = re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣa-zA-Z]', ' ', text)
    return text


sample_content = preprocessing(sample_content)
# print(sample_content[:1000])


tokenizer = RegexTokenizer()
# print(tokenizer)

# 전처리 이전의 샘플 텍스트로 토큰화
tokened_title = tokenizer.tokenize(sample_title)
# print(tokened_title)

# 전처리 이후의 샘플 텍스트로 토큰화
tokened_content = tokenizer.tokenize(sample_content)
print(tokened_content[:10])

print(len(tokened_title))
print(len(tokened_content))

sentences = df['조리법'].apply(preprocessing)

tokens = sentences.apply(tokenizer.tokenize)
print(tokens[:])

print(tokens[sample_index][:10])

# word2vec 모델 학습에 로그를 찍을 수 있도록 합니다.
import logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

# 초기화 및 모델 학습
from gensim.models import word2vec

# 모델 학습
model = word2vec.Word2Vec(tokens, min_count=0)
model.save('word2vec_syn.model')

### 재료사전 불러오기
df2 = pd.read_excel('재료사전.xlsx')

## 재료사전 전처리
# 한글만 남기고 공백 제거
df2['재료'] = df2['재료'].apply(lambda x: re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣]', '', x))

# 중복된 데이터의 빈도수 합치기
df2 = df2.groupby('재료').sum().reset_index()
# df2 = df2.groupby('재료', as_index=False)['재료'].sum()

df2.sort_values(by=['빈도수'],ascending=False,inplace=True,ignore_index=True)
# print(df2)
df2 = df2[(df2['빈도수']>=250)]

for i in range(len(df2)):
    try:
      ingredient = df2.at[i, '재료']
      # print(ingredient)
      result = model.wv.most_similar(ingredient)
      similar_words = [word[0] for word in result if word[1] >= 0.8]
      for j in range(i+1, len(df2)):
        if df2['재료'][j] in similar_words:
          print('--> {0} replaced with {1}'.format(df2['재료'][j], df2['재료'][i]))
          df2['재료'][j] = df2['재료'][i]


    except KeyError:
        pass



df2 = df2.groupby('재료').sum().reset_index()
# df2 = df2.groupby('재료', as_index=False)['재료'].sum()

df2 = df2.sort_values(by=['빈도수'],ascending=False)
print(df2)

# 데이터프레임 엑셀로 저장
df2.to_excel('재료사전_유의어ver3.xlsx')

