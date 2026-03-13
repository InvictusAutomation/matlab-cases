import numpy as np
from scipy.optimize import fsolve
f=lambda x: [x[0]**2+x[1]**2-1, x[0]-x[1]]
print(fsolve(f, [1,1]))