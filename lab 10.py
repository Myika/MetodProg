import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares

def func(x):
    return x**2 * np.sin(x)

x = np.array([i * 0.1 for i in range(1, 11)])
y = np.array([func(xi) for xi in x])

print('x=', x)
print('y=', y)

def fun(a, x, y):
    return a[0] * x**2 * np.sin(x) - y

a0 = np.array([1])

res_lsq = least_squares(fun, x0=a0, args=(x, y))

print("a0 = %.2f" % res_lsq.x[0])

f = lambda x: res_lsq.x[0] * x**2 * np.sin(x)
x_p = np.linspace(min(x), max(x), 100)
y_p = f(x_p)

plt.plot(x, y, 'o')
plt.plot(x_p, y_p, 'b')
plt.title("МНК_наближення прямою")
plt.grid(True)
plt.show()