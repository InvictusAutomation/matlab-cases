import numpy as np
from scipy.integrate import solve_ivp
events=lambda t, y: y-2
sol=solve_ivp(lambda t, y: -y, [0, 5], [1], events=[events])
print('Event detected')