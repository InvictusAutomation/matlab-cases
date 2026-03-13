import numpy as np
A = np.array([[4,3,2],[2,3,4],[1,1,1]])
P, L, U = np.linalg.lu(A)
print('LU Decomposition:')