import numpy as np
c=[1,2,3,4]; H=np.column_stack([c,np.roll(c,-1)]); print(H[:,:-1])