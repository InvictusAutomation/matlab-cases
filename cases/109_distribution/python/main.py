import numpy as np
from scipy import stats
x=np.random.randn(100); mu,sigma=stats.norm.fit(x); print(mu,sigma)