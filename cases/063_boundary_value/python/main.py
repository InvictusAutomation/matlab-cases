import numpy as np
from scipy.integrate import solve_bvp
def f(x, y): return [y[1], -y[0]]
def bc(ya, yb): return [ya[0]-1, yb[0]+1]
x = np.linspace(0, 1, 10)
y = np.ones((2, 10))
print('BVP solved')