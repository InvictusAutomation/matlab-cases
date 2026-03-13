import numpy as np
from scipy.integrate import quad
I, _ = quad(lambda x: np.sin(x), 0, np.pi)
print(I)