import numpy as np
from scipy import stats
groups=[np.random.randn(30), np.random.randn(30), np.random.randn(30)]
print(stats.f_oneway(*groups))