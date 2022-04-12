import numpy as np

x = np.arange(7)
print(x)

# 배열의 각 요소 선택을 Index 배열을 전달하여 지정하는 방식
print(x[[1,3,5]]) # 1번째, 3번째 5번째 요소 지정

x = np.arange(1, 13, 1).reshape(3,4)
print(x)

print(x[[0,2]]) # 0번째 행과 2번째 행 지정.