import numpy as np
import math
from scipy.misc import derivative
def f(x):
    return x**4 - 12*x**3 - 9

def komb(a,b,eps):
    if (derivative(f, a, n = 1)*derivative(f, a, n = 2)>0):
        a0 = a
        b0 = b
       
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai-bi)>eps:   
        ai_1 = ai -f(ai)*(bi - ai)/(f(bi) - f(ai))
        bi_1 = bi - f(bi)/derivative(f,bi, n= 1) 
        ai = ai_1
        bi = bi_1
    x = (ai_1+bi_1)/2 
 
    return print('Розв’язування рівняння комбінованим методом x = ', x)
komb(-2,-1/2,0.0001)

