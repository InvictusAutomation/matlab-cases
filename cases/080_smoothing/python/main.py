import numpy as np
from scipy.signal import savgol_filter
import numpy as np
y=np.sin(np.arange(100)/10)+np.random.randn(100)*0.1
ys=savgol_filter(y, 11, 3)
print('Smoothed')