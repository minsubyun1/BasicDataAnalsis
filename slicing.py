import numpy as np
x = np.arange(7)
print(x)

print(x[1:4]) # [1 2 3] 인덱스 1번째부터 4-1번째까지
print(x[1:]) # [1 2 3 4 5 6]
print(x[:4]) # [0 1 2 3] 인덱스 0번째부터 4-1번째까지
print(x[::2]) # [0 2 4 6] 인덱스 2의 배수번째만 

x = np.arange(1, 13, 1)
x.shape = 3, 4
print(x)

print(x[1:2, :2:3] ) # 1행부터 2-1행까지, 2열과 3열 전까지
print(x[0:,:2:3]) # 0행부터 끝까지, 2열의 -1열까지 즉 1열까지
print(x[1:, :2]) # 1행부터 끝까지, 2-1열까지 
