import numpy as np
import pandas as pd
# 데이터프레임 분석용 함수
# 집계함수 count 
# count 메서드 활용하여 데이터 갯 확인 가능(Default: NaN 값 제외)

data = {
    'korean' : [50, 60, 70],
    'math': [10, np.nan, 40]
}
df = pd.DataFrame(data, index = ['a', 'b', 'c'])
print(df.count(axis = 0)) # 열 기준
print(df.count(axis = 1)) # 행 기준

# max,min 최대, 최소(Default: 열 기준, NaN 값 제외)
df.max()
df.min()

# sum, mean 메서드로 합계 및 평균 계산

df.sum()
df.mean()

# axis, skipna 인자 활용하여 합계 및 평균 계산
print(df.sum(axis = 1)) # 행 기준 합계
print(df.mean(axis = 1, skipna=False)) # 행 기준 합계, NaN 값 포함

# NaN 값이 존재하는 column의 평균 구하여 NaN 값 대체
B_avg = df['math'].mean()
print(B_avg)

# NaN 값 대체
df['math'] = df['math'].fillna(B_avg)
# 평균
print(df.mean(axis = 1, skipna=False))
