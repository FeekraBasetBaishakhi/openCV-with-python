# crop 'feekra'

import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'cat.jpg'))

print(img.shape)

crop_img = img[35:250, 140:390]

cv2.imshow('img', img)
cv2.imshow('crop_img', crop_img)
cv2.waitKey(0)