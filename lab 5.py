import math 

x0 = 0.1
y0 = -0.2
delta = 0.001 

def f1(x, y):
    return math.cos(x + 1) / (2 * y)

def f2(y):
    return -0.4 - math.sin(y)


x = -0.075
y = -0.2


epsilon = 0.001

while True:
    x_new = f1(x, y)
    y_new = f2(y)
    
    if abs(x_new - x) < epsilon and abs(y_new - y) < epsilon:
        break

    x, y = x_new, y_new

print("Розв'язок:")
print(f"x = {x}")
print(f"y = {y}")