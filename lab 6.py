import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x = np.array([-3., -2., 0., 2.], dtype=float)
y = np.array([-22., -13., -7., 23.], dtype=float)
x_test = [-4, -1.5, -1, 1.5]

def lagrange_interpolation(x, y, x_test):
    n = len(x)
    results = []

    for test in x_test:
        p = np.zeros(n)
        for i in range(n):
            p_i = 1
            for j in range(n):
                if i != j:
                    p_i *= (test - x[j]) / (x[i] - x[j])
            p[i] = p_i
        result = round(np.dot(y, p), 4)
        results.append(result)
        print(f"Значення функції {test} = {result}")

    return results

f_interp = lagrange_interpolation(x, y, x_test)

xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagrange(x, y)(i) for i in xnew]

plt.plot(x, y, 'o', xnew, ynew)
plt.title('Lagrange Polynomial_1')
plt.grid(True)
plt.show()

f = lagrange(x, y)

fig = plt.figure(figsize=(7, 5))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial_2')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()