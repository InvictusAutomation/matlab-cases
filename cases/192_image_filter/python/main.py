import numpy as np
import cv2, numpy as np
img=np.random.randint(0,255,(100,100,3),dtype=np.uint8)
filtered=cv2.GaussianBlur(img,(5,5),1)
print(filtered.shape)