#!/usr/bin/env python3
"""
001_matrix_basic - 矩阵基础运算
演示Python中矩阵的创建、基本运算和操作
"""

import numpy as np

def main():
    # 1. 矩阵创建
    A = np.array([[1, 2, 3], 
                  [4, 5, 6], 
                  [7, 8, 9]])  # 3x3矩阵
    B = np.eye(3)                # 3x3单位矩阵
    C = np.zeros((3, 3))        # 3x3零矩阵
    D = np.ones((3, 3))         # 3x3全1矩阵
    E = np.random.rand(3, 3)   # 3x3随机矩阵
    
    # 2. 矩阵运算
    F = A + B                   # 矩阵加法
    G = A - B                   # 矩阵减法
    H = A @ B                   # 矩阵乘法
    I = A * B                   # 元素乘法
    J = np.linalg.solve(A, B)   # 矩阵右除 (A@X=B)
    K = np.linalg.solve(B, A)   # 矩阵左除 (B@X=A)
    
    # 3. 矩阵转置和逆
    L = A.T                     # 转置
    M = np.linalg.inv(A)        # 逆矩阵
    N = np.linalg.pinv(A)        # 伪逆
    
    # 4. 输出结果
    print("矩阵A:")
    print(A)
    print("\n矩阵B:")
    print(B)
    print("\nA+B:")
    print(F)
    print("\nA@B:")
    print(H)
    print("\nA的转置:")
    print(L)

if __name__ == "__main__":
    main()
