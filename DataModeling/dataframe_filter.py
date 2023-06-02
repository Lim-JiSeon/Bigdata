import numpy as np
import pandas as pd
import os
import re


# 폴더 내에 있는 엑셀 파일 한번에 열기
path = 'C:/Users/ksc/Desktop/음식레시피_전처리/음식레시피/1. 소요시간, 난이도 필터링/'
file_list = os.listdir(path)
file_list_py = [file for file in file_list if file.endswith('.xlsx')]


# open한 파일을 하나의 데이터프레임으로 합치기
df = pd.DataFrame()
for i in file_list_py:
    print(i)
    data = pd.read_excel(path + i)
    # 3인분 이하인 레시피만 추출하기
    filtered_df = data[data['인분'].str.contains('인분')].copy()  # '인분' 칼럼 값에 '인분'이 포함된 데이터만 필터링
    filtered_df = filtered_df[filtered_df['인분'] <= '3인분']  # 3인분 이하인 데이터 추출

    # filtered_df['인분'] = filtered_df['인분'].str.extract(r'(\d+)')  # '인분' 값에서 숫자만 추출
    # filtered_df['인분'] = filtered_df['인분'].astype(int)  # 추출한 숫자를 정수형으로 변환
    # filtered_df = filtered_df[filtered_df['인분'] <= 3]  # 3인분 이하인 데이터 추출
    # df['주거타입'] = extract_tradeType(str(path + i))
    df = pd.concat([df, filtered_df])

print(df)
df.to_csv('C:/Users/ksc/Desktop/음식레시피_전처리/음식레시피/1. 소요시간, 난이도 필터링/조리법_필터링ver2.csv', encoding='utf-8', index = None)


