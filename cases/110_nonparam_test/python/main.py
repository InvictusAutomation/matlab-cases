import numpy as np
from scipy import stats
x,y=np.random.randn(50), np.random.randn(50)
print(stats.mannwhitneyu(x,y))