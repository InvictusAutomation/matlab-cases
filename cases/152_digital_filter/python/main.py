import numpy as np
from scipy.signal import lfilter
b,a=[1,0.5],[1,0.2,0.3]; x=np.random.randn(100)
print(lfilter(b,a,x)[:10])