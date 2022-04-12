import numpy as np

x = np.arange(7)

# Boolean mask? True, False로 구성된 mask array
print(x)
print(x < 3)
print(x > 7)
print(x[x < 3])
print(x[x % 2== 0])