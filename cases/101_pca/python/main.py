#!/usr/bin/env python3
"""
101_pca - 主成分分析
使用sklearn进行PCA分析
"""

import numpy as np
from sklearn.decomposition import PCA

# 生成样本数据
np.random.seed(42)
X = np.random.randn(100, 5) * 2 + np.ones((100, 5))

# PCA分析
pca = PCA(n_components=3)
score = pca.fit_transform(X)
coeff = pca.components_.T
latent = pca.explained_variance_

print("主成分系数 (前3个):")
print(coeff[:, :3])
print("\n主成分得分 (前5个):")
print(score[:5, :])
print(f"\n方差解释比例: {pca.explained_variance_ratio_ * 100}")
