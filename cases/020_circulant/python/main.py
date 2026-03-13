import numpy as np
c=np.array([1,2,3,4]); A=np.column_stack([np.roll(c,-i) for i in range(4)])