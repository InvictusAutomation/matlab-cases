import numpy as np
from sklearn.linear_model import HuberRegressor
X=np.arange(10).reshape(-1,1); y=np.array([1,2,4,3,5,6,8,7,9,10]);
h=HuberRegressor().fit(X,y); print(h.coef_)