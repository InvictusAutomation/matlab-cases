import numpy as np
from scipy.signal import hilbert
x=np.sin(np.linspace(0,10,100)); analytic=hilbert(x); print(analytic[:10])