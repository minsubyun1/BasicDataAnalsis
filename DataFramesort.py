from numpy import NaN
import pandas as pd




df = pd.DataFrame(columns=['col1', 'col2', 'col3'])
df.loc[1] = [1, 'A', 1]
df.loc[0] = [2, 'A', 0]
df.loc[2] = [9, 'B', 9]
df.loc[3] = [8, NaN, 4]
df.loc[4] = [7, 'D', 2]
df.loc[5] = [4, 'C', 3]

#index 값 기준으로 정렬하기
# axis = 0 : 행 인덱스 기준 정렬(Default 오름차순)

df = df.sort_index(axis = 0)

# axis = 1 : 열 인덱스 기준 내림차순 정렬

print(df.sort_index(axis = 1, ascending=False))

# Column 값 기준으로 정렬
# col1 컬럼 기준 정렬(Default 오름차순)
print(df.sort_values('col1', ascending=True))
# col1 컬럼 기준 내림차순 정렬
print(df.sort_values('col1', ascending=False))
# col2 컬럼 기준 오름차순 정렬 후 col2 컬럼 기준 내림차순 정렬
print(df.sort_values(('col2'), ascending=True))
print(df.sort_values(['col2', 'col1'], ascending=[True, False]))