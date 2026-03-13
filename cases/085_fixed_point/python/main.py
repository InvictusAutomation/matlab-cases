import numpy as np
g=lambda x: (x+2/x)/2
x=1
for i in range(10): x=g(x)
print(x)