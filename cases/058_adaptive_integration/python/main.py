import numpy as np
from scipy.integrate import quad
I, _ = quad(lambda x: np.sin(1/x), 0.001, 1)
print(I)