import numpy as np
from scipy import integrate

def f(x):
    return np.cos(x) / (x + 2)

a = 0.4
b = 1.2

n = 8

def adaptive_simpson_rule(f, a, b, tol=1e-6):
    h = (b - a) / n
    integral1 = h / 3 * (f(a) + 4 * f((a + b) / 2) + f(b))
    return recursive_adaptive_simpson(f, a, b, tol, integral1, f(a), f((a + b) / 2), f(b))

def recursive_adaptive_simpson(f, a, b, tol, integral1, fa, fc, fb):
    c = (a + b) / 2
    h = (b - a) / 2
    d = (a + c) / 2
    e = (c + b) / 2
    fd = f(d)
    fe = f(e)

    integral2 = h / 3 * (fa + 4 * fd + fc)
    integral3 = h / 3 * (fc + 4 * fe + fb)

    if np.abs(integral2 + integral3 - integral1) <= 15 * tol:
        return integral2 + integral3
    else:
        tol /= 2
        return (
            recursive_adaptive_simpson(f, a, c, tol, integral2, fa, f((a + c) / 2), fc) +
            recursive_adaptive_simpson(f, c, b, tol, integral3, fc, f((c + b) / 2), fb)
        )

result = adaptive_simpson_rule(f, a, b)

print("Адаптивний метод Сімпсона:", round(result, 6))

v, err = integrate.quad(f, a, b)
print("Перевірте наявність адаптивного методу Сімпсона:", round(v, 6))