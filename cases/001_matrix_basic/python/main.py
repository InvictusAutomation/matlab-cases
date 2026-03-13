import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.eye(3)
C = A + B
D = A @ B
E = A.T
print('Matrix operations completed')
print(C)