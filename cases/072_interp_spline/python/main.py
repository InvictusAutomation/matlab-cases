import numpy as np
from scipy.interpolate import interp1d
x=np.arange(5); y=np.arange(0,9,2); f=interp1d(x,y,'cubic')
print(f(2.5))