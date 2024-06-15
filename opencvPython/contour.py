import os

import cv2

img = cv2.imread(os.path.join('.',  'data', 'birds.jpg'))

ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)

