import numpy as np
from scipy.signal import windows
print(windows.hamming(256)[:10])