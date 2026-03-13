import numpy as np
A=np.array([[1,2],[3,4]]); b=np.array([5,11]); Q,R=np.linalg.qr(A); x=np.linalg.solve(R,Q.T@b)