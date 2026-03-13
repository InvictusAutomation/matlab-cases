import numpy as np
from scipy.optimize import curve_fit
x=np.arange(6); y=np.exp(-x)
def f(x,a,b): return a*np.exp(-b*x)
print(curve_fit(f, x, y))