from scipy import integrate
import numpy as np

eps = 0.001
a = 0.4
b = 1.2

def f2(x): 
    return 1 / np.sqrt(x + 3)

def left_rec(f, a, b, n): 
    h = (b - a) / n 
    _sum = 0 
    for i in range(0, n): 
        _sum += f(a + i * h) 
    return _sum * h 

if abs(left_rec(f2, a, b, 2 * 10) - left_rec(f2, a, b, 10)) / 3. <= eps:
    print("Лівий прямокутник:", round(left_rec(f2, a, b, 10), 5)) 

def right_rec(f, a, b, n): 
    h = (b - a) / n 
    _sum = 0 
    for i in range(1, n + 1): 
        _sum += f(a + i * h) 
    return _sum * h 

print("Правильний прямокутник:", round(right_rec(f2, a, b, 10), 5)) 

def aver_rec(f, a, b, n): 
    h = (b - a) / n 
    _sum = 0 
    for i in range(0, n): 
        _sum += f(a + i * h) 
    return _sum * h 

print("Середній прямокутник:", round(aver_rec(f2, a, b, 10), 5)) 

result_quad, _ = integrate.quad(f2, a, b)
print("Результат четвірки:", round(result_quad, 5))