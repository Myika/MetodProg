import numpy as np

a = np.array([[1, 2, -1],[3, 4, 1],[5, 1, -3]])

a1= np.linalg.det(a)

b = np.array([-3, 1, -2])

x = []

for i in range(len(a)):
    ai = a.copy()
    ai[:, i] = b
    a1i = np.linalg.det(ai)
    


    xi = a1i / a1
    x.append(xi)

x = np.array(x)

print("Крамера:")
print(x)

q= np.linalg.solve(a, b)

print("Solve() з пакету linalg:")
print(q)