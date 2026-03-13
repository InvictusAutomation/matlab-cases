import numpy as np
v=np.array([1,2,3]); H=np.eye(3)-2*np.outer(v,v)/np.dot(v,v); print(H)