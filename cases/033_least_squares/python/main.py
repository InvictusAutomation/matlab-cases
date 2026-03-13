import numpy as np
X=np.array([[1,1],[1,2],[1,3]]); y=np.array([1,2,3]); print(np.linalg.lstsq(X,y,rcond=None)[0])