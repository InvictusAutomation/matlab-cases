import numpy as np
import cv2, numpy as np
img=np.random.randint(0,2,(50,50),dtype=np.uint8)*255
kernel=np.ones((3,3),np.uint8)
opened=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
print(opened.shape)