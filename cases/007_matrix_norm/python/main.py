import numpy as np
A = np.array([[1,2],[3,4]])
n1 = np.linalg.norm(A, 1)
n2 = np.linalg.norm(A, 2)
nF = np.linalg.norm(A, 'fro')
print(n1, n2, nF)