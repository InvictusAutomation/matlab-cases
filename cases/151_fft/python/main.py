#!/usr/bin/env python3
"""
151_fft - 快速傅里叶变换
使用numpy进行频谱分析
"""

import numpy as np
import matplotlib.pyplot as plt

# 生成信号
Fs = 1000                    # 采样频率
t = np.arange(0, 1, 1/Fs)    # 时间向量
f1, f2 = 50, 120             # 信号频率
x = np.sin(2*np.pi*f1*t) + 0.5*np.sin(2*np.pi*f2*t)

# FFT变换
N = len(x)
Y = np.fft.fft(x)
P2 = np.abs(Y/N)
P1 = P2[:N//2+1]
P1[1:-1] = 2*P1[1:-1]
f = Fs * np.arange(0, N/2) / N

# 绘制频谱
plt.figure(figsize=(10, 6))
plt.plot(f, P1)
plt.xlabel('频率 (Hz)')
plt.ylabel('幅值')
plt.title('信号频谱')
plt.grid(True)
plt.savefig('spectrum.png', dpi=100)
plt.show()

print(f"峰值频率: {f[np.argmax(P1[1:])+1]} Hz")
