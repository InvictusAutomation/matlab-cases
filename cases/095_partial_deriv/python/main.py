import numpy as np
f=lambda x,y: x**2+y**2
h=0.01
print((f(1+h,1)-f(1-h,1))/(2*h))