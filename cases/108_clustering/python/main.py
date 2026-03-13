import numpy as np
from sklearn.cluster import KMeans
X=np.random.randn(100,5); print(KMeans(n_clusters=3).fit_predict(X)[:10])