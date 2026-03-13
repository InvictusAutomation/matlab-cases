import scipy.linalg as la
expm=la.expm
A=np.array([[0,1],[0,0]]); print(expm(A))