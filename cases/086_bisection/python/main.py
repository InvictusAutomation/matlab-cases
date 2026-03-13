import numpy as np
f=lambda x: x**2-2
a,b=1,2
for i in range(50): m=(a+b)/2; b=m if f(m)>0 else a=m
print((a+b)/2)