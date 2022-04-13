import numpy as np
import pandas as pd

df = pd.DataFrame({
    'data1' : range(6),
    'data2' : [4,4,6,0,6,1],
    'key' : ['A', 'B', 'C', 'A','B','C']
})
# 간단한 집계를 넘어서, 조건부로 집계하고 싶은 경우
df.groupby('key').sum() # key 그룹별 합계
df.groupby(['key', 'data1']).sum() # key와 데이터1 그룹별 합계

# groupby를 통해서 집계를 한번에 계산하는 방법
# aggregate
df.groupby('key').aggregate(['min', np.median, max])
df.groupby('key').aggregate({'data1':'min', 'data2':np.sum}) 

# filter
# groupby를 통해서 그룹 속성을 기준으로 데이터 필터링

def filter_by_mean(x):
    return x['data2'].mean() > 3
df.groupby('key').mean()
df.groupby('key').filter(filter_by_mean)

# apply.lambda
# groupby를 통해서 묶인 데이터에 함수 적용

df.groupby('key').apply(lambda x: x.max() - x.min())

# get_group 
# groupby로 묶인 데이터에서 key 값으로 데이터를 가져올 수 있다.

# df = pd.read_csv("./univ.csv")

# 상위 5개 데이터
# df.head()

# 데이터 추출
# df.groupby("시도").get_group("충남")
# len(df.groupby("시도").get_group("충남")) 
# 94