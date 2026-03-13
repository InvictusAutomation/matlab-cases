import numpy as np
from scipy.signal import stft
x=np.random.randn(1024); f,t,Zxx=stft(x); print(Zxx.shape)