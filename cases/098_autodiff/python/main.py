import numpy as np
import autograd
f=lambda x: x**2+np.sin(x)
grad_f=autograd.grad(f)
print(grad_f(1.0))