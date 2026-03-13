import numpy as np
import cv2, numpy as np
img=np.random.randint(0,255,(100,100),dtype=np.uint8)
edges=cv2.Canny(img,100,200)
print(edges.shape)