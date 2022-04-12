import numpy as np
x = np.arange(7)
print(x)
print(x[3])
#print(x[7])

x[0] = 10
print(x)

x= np.arange(1, 13, 1)
x.shape= 3,4 #1에서 13-1까지 3, 4 형태의 행렬로
# [[1 2 3 4]
#  [5 6 7 8]
#  [9 10 11 12]]

print(x[2,3])
