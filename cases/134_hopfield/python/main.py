#!/usr/bin/env python3
"""
134_hopfield - Python Implementation
This is a template file
"""

import numpy as np

def main():
    print("134_hopfield")
    
    # Your code here
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    # Matrix operations
    C = A @ B
    
    print("Result:")
    print(C)

if __name__ == "__main__":
    main()
