import numpy as np
from scipy.integrate import solve_ivp
f=lambda t, y: -y
sol=solve_ivp(f, [0, 10], [1], method='Radau')
print(sol.y[0,-1])