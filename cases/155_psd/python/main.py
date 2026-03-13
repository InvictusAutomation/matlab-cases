import numpy as np
from scipy.signal import periodogram
x=np.random.randn(1024); print(periodogram(x)[0][:10])