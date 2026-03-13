import numpy as np
from sklearn.linear_model import LassoCV
X,y=np.random.randn(100,10), np.random.randn(100)
print(LassoCV().fit(X,y).alpha_)