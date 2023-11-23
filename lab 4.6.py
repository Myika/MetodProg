import numpy as np
a = np.matrix('1 2 -3; 0 1 2; 0 0 1')
b = np.linalg.inv(a)
print(b)