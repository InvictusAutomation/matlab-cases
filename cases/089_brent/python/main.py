import numpy as np
from scipy.optimize import brentq
f=lambda x: x**2-2
print(brentq(f, 1, 2))