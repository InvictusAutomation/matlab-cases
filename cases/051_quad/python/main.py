import numpy as np
from scipy.integrate import quad
f=lambda x: x**2
I, _ = quad(f, 0, 1)
print(I)