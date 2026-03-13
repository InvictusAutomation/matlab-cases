import numpy as np
A=np.array([[1,2],[3,4]]); b=np.array([5,11]); U,S,V=np.linalg.svd(A,full_matrices=False); x=V@(U.T@b)/S; print(x)