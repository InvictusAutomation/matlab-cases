import numpy as np
import pywt
cA,cD=pywt.dwt([1,2,3,4],'haar'); print(cA)