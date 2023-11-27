import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model1(y, x):
    dydx = x + np.cos(y/np.sqrt(2))
    return dydx

y0_1 = 1.4
x_range_1 = [0.8, 1.8]

x1 = np.linspace(x_range_1[0], x_range_1[1], 100)

y1 = odeint(model1, y0_1, x1)

plt.figure()
plt.plot(x1, y1)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Розв’язання диф. рівняння y\' = x + cos(y/sqrt(2))')
plt.grid()
plt.show()

def model2(y, x):
    dydx = x + np.sin(y/np.pi)
    return dydx

y0_2 = 5.3
x_range_2 = [1.7, 2.7]

x2 = np.linspace(x_range_2[0], x_range_2[1], 100)

y2 = odeint(model2, y0_2, x2)


plt.figure()
plt.plot(x2, y2)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Розв’язання диф. рівняння y\' = x + sin(y/π)')
plt.grid()
plt.show()