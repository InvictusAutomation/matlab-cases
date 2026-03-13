import numpy as np
import pywt
x=np.random.randn(100)+np.sin(np.linspace(0,10,100)); c=pywt.wavedec(x,'db4',level=3); print('denoised')