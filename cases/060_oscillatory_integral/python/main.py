import numpy as np
from scipy.integrate import quad
I, _ = quad(lambda x: np.sin(10*x)/x, 0, np.inf)
print(I)