import pandas as pd

# Numpy의 array가 보강된 형태로서 Data와 Index를 가지고 있다.

data = pd.Series([1,2,3,4])
print(data)

# Series는 값을 ndarray, 즉 다차원 행렬 구조 형태로 가지고 있다.
print(type(data))
print(data.values)
print(type(data.values))

#dtype 인자로 데이터 타입을 지정할 수 있다.
data = pd.Series([1,2,3,4], dtype ="float")
print(data.dtype)

#인덱스를 지정할 수 있고 인덱스로 접근 가능
data = pd.Series([1,2,3,4], index=['a', 'b', 'c', 'd'])
data['c'] = 5 #인덱스로 접근하여 요소 변경 가능
print(data)