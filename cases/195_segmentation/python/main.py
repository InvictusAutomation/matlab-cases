import numpy as np
from skimage.segmentation import slic
import numpy as np
img=np.random.randint(0,255,(100,100,3),dtype=np.uint8)
segments=slic(img,n_segments=50)
print(len(np.unique(segments)))