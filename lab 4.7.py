import numpy as np
a = np.matrix('1 -1 3 4; 0 -1 2 1; 1 1 -1 2; 2 3 -5 3')
b = np.linalg.matrix_rank(a)
print(b)