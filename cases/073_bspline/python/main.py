import numpy as np
from scipy.interpolate import splrep, splev
x=np.linspace(0,10,20); y=np.sin(x); tck=splrep(x,y); print(splev(5,tck))