#!/usr/bin/env python3
"""
051_quad - 数值积分
使用scipy.integrate进行数值积分
"""

import numpy as np
from scipy.integrate import quad

def f(x):
    return x**2

# 计算积分 ∫₀¹ x² dx
I, error = quad(f, 0, 1)

print(f"∫₀¹ x² dx = {I:.6f}")
print(f"精确值: {1/3:.6f}")
print(f"误差: {abs(I - 1/3):.10f}")
