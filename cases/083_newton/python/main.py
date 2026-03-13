import numpy as np
f=lambda x: x**2-2
df=lambda x: 2*x
x=1
for i in range(10): x=x-f(x)/df(x)
print(x)