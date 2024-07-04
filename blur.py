# feekra
import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'girl.jpg'))

f_size = 9
img_blur = cv2.blur(img, (f_size, f_size))
img_gaussian_blur = cv2.GaussianBlur(img,(f_size, f_size), 5)
img_median_blur = cv2.medianBlur(img, f_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)