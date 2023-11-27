import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + np.cos(y / np.sqrt(2))

a = 0.8
b = 1.8  
h = 0.1 
y0 = 1.4  

n = int((b - a) / h)  

x = np.array([a + i * h for i in range(n + 1)])  

y = np.empty(n + 1)
y[0] = y0

for i in range(n):
    y[i + 1] = y[i] + f(x[i], y[i]) * h

y_rounded = np.round_(y, 4)
print("x=", x, "\ny=", y_rounded)

plt.plot(x, y, "o-", label="розв'язок")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Метод Ейлера для y'=x+cos(y/sqrt(2))")
plt.legend()
plt.grid()
plt.show()