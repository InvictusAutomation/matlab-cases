import numpy as np
from scipy.integrate import tplquad
I, _ = tplquad(lambda x,y,z: x+y+z, 0, 1, 0, 1, 0, 1)
print(I)