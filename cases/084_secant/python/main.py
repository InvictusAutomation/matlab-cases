import numpy as np
f=lambda x: x**2-2
x0, x1 = 1, 2
for i in range(10): x2=x1-f(x1)*(x1-x0)/(f(x1)-f(x0)); x0,x1=x1,x2
print(x1)