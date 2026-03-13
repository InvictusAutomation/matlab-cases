import numpy as np
n=5; W=np.eye(n)*np.ceil(n/2); W=np.diag(np.arange(1,n+1),1)+np.diag(np.arange(n-1,0,-1),-1); print(W)