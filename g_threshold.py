# feekra
import os
import cv2
# calling the path

img = cv2.imread(os.path.join('.', 'data', 'panda.jpg'))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
thresh = cv2.blur(thresh, (10,10))
# visualize image
cv2.imshow('img', img)
cv2.imshow('img_gray', img_gray)
cv2.imshow('thresh', thresh)

cv2.waitKey(0)

