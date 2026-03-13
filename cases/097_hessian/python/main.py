import numpy as np
from scipy.optimize import approx_fprime
import numpy as np
f=lambda x: x[0]**2+x[0]*x[1]+x[1]**2
def hess(x): return [[2,1],[1,2]]
print(hess([1,1]))