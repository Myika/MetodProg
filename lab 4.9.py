import numpy as np
n = int(input())
m = int(input())

a = np.random.randint(0, 100, size=(n, m))

serznkoz = np.mean(a, axis=1)
serzn = np.min(serznkoz)

print("Матриця:")
print(a)
print("Середні значення для кожного рядка:")
print(serznkoz)
print("Найнижче середнє значення:", serzn)