import numpy as np
f=lambda x: x**2
h=0.01
print((f(1+h)-f(1-h))/(2*h))