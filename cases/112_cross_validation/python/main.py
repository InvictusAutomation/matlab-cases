import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
X,y=np.random.randn(100,3), np.random.randn(100)
print(cross_val_score(LinearRegression(), X, y, cv=5))