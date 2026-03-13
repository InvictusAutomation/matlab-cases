#!/usr/bin/env python3
"""
002_lu_decomposition - LU分解
将方阵A分解为下三角矩阵L和上三角矩阵U
"""

import numpy as np
from scipy.linalg import lu

def main():
    # 定义矩阵A
    A = np.array([[4, 3, 2], 
                  [2, 3, 4], 
                  [1, 1, 1]], dtype=float)
    
    # LU分解
    P, L, U = lu(A)
    
    # 显示结果
    print("原矩阵A:")
    print(A)
    print("\n置换矩阵P:")
    print(P)
    print("\n下三角矩阵L:")
    print(L)
    print("\n上三角矩阵U:")
    print(U)
    print("\nP@L@U:")
    print(P @ L @ U)
    
    # 使用LU分解求解线性方程组 Ax = b
    b = np.array([7, 6, 3])
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    print("\n解向量x:")
    print(x)

if __name__ == "__main__":
    main()
