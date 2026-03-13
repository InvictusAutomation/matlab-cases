import numpy as np
f=lambda x: np.sin(x)
h=0.01
print((f(1+h)-2*f(1)+f(1-h))/h**2)