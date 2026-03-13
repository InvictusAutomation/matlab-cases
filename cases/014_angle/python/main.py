import numpy as np
a=np.array([1,0]); b=np.array([1,1]); theta=np.arccos(np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))); print(np.degrees(theta))