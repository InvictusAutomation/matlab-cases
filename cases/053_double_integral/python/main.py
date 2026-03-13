import numpy as np
from scipy.integrate import dblquad
I, _ = dblquad(lambda x,y: x+y, 0, 1, 0, 1)
print(I)