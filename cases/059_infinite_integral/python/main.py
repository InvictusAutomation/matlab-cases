import numpy as np
from scipy.integrate import quad
I, _ = quad(lambda x: np.exp(-x**2), 0, np.inf)
print(I)