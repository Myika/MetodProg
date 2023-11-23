import numpy as np
a = np.matrix('2 3 4 1; 1 2 3 4; 3 4 1 2; 4 1 2 3')
b = np.linalg.det(a)
print(b)