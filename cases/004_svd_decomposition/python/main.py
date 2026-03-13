#!/usr/bin/env python3
"""
004_svd_decomposition - 奇异值分解SVD
将矩阵A分解为U@S@V.T
"""

import numpy as np

def main():
    # 定义矩阵A
    A = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6]], dtype=float)
    
    # SVD分解
    U, S, V = np.linalg.svd(A, full_matrices=False)
    
    # 显示结果
    print("原矩阵A:")
    print(A)
    print("\n左奇异向量U:")
    print(U)
    print("\n奇异值S:")
    print(S)
    print("\n右奇异向量V:")
    print(V)
    
    # 重构矩阵
    A_reconstructed = U @ np.diag(S) @ V
    print("\n重构矩阵:")
    print(A_reconstructed)

if __name__ == "__main__":
    main()
