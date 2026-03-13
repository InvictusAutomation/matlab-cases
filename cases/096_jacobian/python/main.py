import numpy as np
from scipy.optimize import approx_fprime
f=lambda x: [x[0]**2, x[1]**2-x[0]]
print(approx_fprime([1,1], f, 0.01))