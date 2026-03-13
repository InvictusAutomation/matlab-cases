#!/usr/bin/env python3
"""
003_qr_decomposition - QR分解
将矩阵A分解为正交矩阵Q和上三角矩阵R
"""

import numpy as np

def main():
    # 定义矩阵A
    A = np.array([[12, -51, 4], 
                  [6, 167, -68], 
                  [-4, 24, -41]], dtype=float)
    
    # QR分解
    Q, R = np.linalg.qr(A)
    
    # 显示结果
    print("原矩阵A:")
    print(A)
    print("\n正交矩阵Q:")
    print(Q)
    print("\n上三角矩阵R:")
    print(R)
    print("\nQ@R:")
    print(Q @ R)
    
    # 验证Q的正交性
    print("\nQ.T @ Q (应为单位矩阵):")
    print(Q.T @ Q)

if __name__ == "__main__":
    main()
