import numpy as np
import numpy as np
N=10; h=1/N
A=np.diag(2*np.ones(N-1))-np.diag(np.ones(N-2),1)-np.diag(np.ones(N-2),-1)
print(A/h**2)