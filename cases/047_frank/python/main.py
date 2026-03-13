import numpy as np
n=4; print(np.eye(n)*np.arange(1,n+1) + np.eye(n)*np.arange(n,0,-1) - np.eye(n))