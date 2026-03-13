import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X,y=np.random.randn(100,5), np.random.randint(0,2,100)
print(LinearDiscriminantAnalysis().fit(X,y).coef_)