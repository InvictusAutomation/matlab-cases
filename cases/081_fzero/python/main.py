import numpy as np
from scipy.optimize import fsolve
f=lambda x: x**2-2
print(fsolve(f, 1))