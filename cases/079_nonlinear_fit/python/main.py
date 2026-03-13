import numpy as np
from scipy.optimize import curve_fit
import numpy as np
x=np.arange(0,1.1,0.1); y=np.exp(-x)
def f(x,a,b): return a*np.exp(-b*x)
print(curve_fit(f, x, y))