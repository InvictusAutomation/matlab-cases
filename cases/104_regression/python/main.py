import numpy as np
from sklearn.linear_model import LinearRegression
X,y=np.random.randn(100,3), np.random.randn(100)
print(LinearRegression().fit(X,y).coef_)