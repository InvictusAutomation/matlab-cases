import numpy as np
A = np.array([[1,2],[3,4],[5,6]])
U, S, V = np.linalg.svd(A)
print('SVD completed')