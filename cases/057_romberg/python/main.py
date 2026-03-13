import numpy as np
from scipy.integrate import romberg
f=lambda x: 1/x
print(romberg(f, 1, 10))