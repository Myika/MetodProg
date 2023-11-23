from scipy import integrate 
import numpy as np

def f(x):
    return 1 / np.sqrt(x**2 - 2)

a = 2.1
b = 3.6
n = 10

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = a + h
    integral = 0
    for i in range(1, n - 1):
        integral += 2 * f(x)
        x += h
    integral += f(b)
    integral *= h / 2

    return integral

integral1 = trapezoidal_rule(f, a, b, n)
n *= 2
integral2 = trapezoidal_rule(f, a, b, n)
while abs(integral2 - integral1) / 3 > 0.001:
    integral1 = integral2
    n *= 2
    integral2 = trapezoidal_rule(f, a, b, n)

print("Tрезультат рапезоїдного методу:", round(integral2, 5))

v, err = integrate.quad(f, a, b)
print("Перевірте метод трапеції:", round(v, 5))