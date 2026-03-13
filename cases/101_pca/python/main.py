import numpy as np
from sklearn.decomposition import PCA
import numpy as np
X=np.random.randn(100,5); pca=PCA(); print(pca.fit_transform(X).shape)