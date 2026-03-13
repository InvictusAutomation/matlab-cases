import numpy as np
from scipy.signal import periodogram
x=np.random.randn(1024); f,Pxx=periodogram(x); print(f[:10])