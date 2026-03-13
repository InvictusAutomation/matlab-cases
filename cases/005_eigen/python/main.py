import numpy as np
A = np.array([[4,2],[1,3]])
w, v = np.linalg.eig(A)
print('Eigenvalues:', w)