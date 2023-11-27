import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + np.sin(y/np.pi)

a = 1.7  
b = 2.7  
h = 0.2  
y0 = 5.3  
n = int((b - a) / h)  

x = np.linspace(a, b, n+1)  

y = np.empty(n+1)
y[0] = y0

for i in range(n):
    y[i+1] = y[i] + h * f(x[i], y[i])

y_rounded = np.round_(y, 4)

print("x =", x, "\ny =", y_rounded)

plt.plot(x, y, "o-", label="Euler-Cauchy")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Ейлера-Коші")
plt.legend(["точки", "y' = x + sin(y/π)"])
plt.grid()
plt.show()