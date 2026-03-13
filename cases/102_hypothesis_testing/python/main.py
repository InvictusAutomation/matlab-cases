import numpy as np
from scipy import stats
x,y=np.random.randn(100), np.random.randn(100)
print(stats.ttest_ind(x,y))