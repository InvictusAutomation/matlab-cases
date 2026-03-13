import numpy as np
from scipy.integrate import solve_ivp
f=lambda t, y: y
sol=solve_ivp(f, [0, 1], [1], method='RK23')
print(sol.y[0,-1])