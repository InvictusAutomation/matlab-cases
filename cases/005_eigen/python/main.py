#!/usr/bin/env python3
"""
005_eigen - 特征值与特征向量
计算矩阵的特征值和特征向量
"""

import numpy as np

def main():
    # 定义矩阵A
    A = np.array([[4, 2], 
                  [1, 3]], dtype=float)
    
    # 特征值分解
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # 显示结果
    print("矩阵A:")
    print(A)
    print("\n特征值:")
    print(eigenvalues)
    print("\n特征向量矩阵:")
    print(eigenvectors)
    
    # 验证AV = VD
    print("\n验证A@V = V@D:")
    print(A @ eigenvectors - eigenvectors @ np.diag(eigenvalues))

if __name__ == "__main__":
    main()
