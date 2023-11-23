import numpy as np 
from scipy.interpolate import CubicSpline 
import matplotlib.pyplot as plt 

x = np.array([0.8, 1, 1.3, 1.9, 2.3])
y = np.array([1.72, 2.35, 1.52, 2.43, 1.55])

n = len(x) - 1
h = np.diff(x)
a = y 
b = np.zeros(n)
d = np.zeros(n)
c = np.zeros(n)

alpha = np.zeros(n)
for i in range(1, n):
    alpha[i]= (3/h[i]) * (a[i+1]-a[i]) - (3/h[i-1]) * (a[i]-a [i-1])

l=np.ones(n)
mu = np.zeros(n)
z = np.zeros(n)

for i in range(1,n):
    l[i]=2*(x[i+1]-x[i-1])-h[i-1]*mu[i-1]
    mu[i]=h[i]/l[i]
    z[i]=(alpha[i]-h[i-1]*z[i-1])/l[i]

c[n-1]=0
b[n-1]=(a[n]-a[n-1])/h[n-1]-h[n-1]*(2*c[n-1]+c[n-2])/3
d[n-1]=(c[n-1]-c[n-2])/(3*h[n-1])

for j in range(n-2,-1,-1):
    c[j]=z[j]-mu[j]*c[j+1]
    b[j]=(a[j+1]-a[j])/h[j]-h[j]*(c[j+1]+2*c[j])/3
    d[j]=(c[j+1]-c[j])/(3*h[j])

for i in range(n):
    print(f"Відрізок {i+1}:")
    print(f"S_{i}(x) = {a[i]} + {b[i].round(4)}(x - {x[i]}) + {c[i].round(4)}(x - {x[i]})^2 + {d[i].round(4)}(x - {x[i]})^3, x належить [{x[i]}, {x[i+1]}]") 



x_values = np.linspace(np.min(x), np.max(x), 100)
y_values = []

for i in range(n):
    mask = (x_values >= x[i]) & (x_values <= x[i +1])
    x_interval=x_values[mask]
    y_interval=a[i]+b[i]*(x_interval-x[i])+c[i]*(x_interval-x[i])**2+d[i]*(x_interval-x[i])**3
    y_values.extend(y_interval)

plt.figure(figsize=(8,8))
plt.plot(x_values, y_values, label="Кубічний сплайн", color='b')
plt.scatter(x, y, label="Задані точки", color='r')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()