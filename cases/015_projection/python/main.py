import numpy as np
a=np.array([1,2]); b=np.array([3,1]); proj = (np.dot(a,b)/np.dot(b,b))*b; print(proj)