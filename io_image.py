import os
import cv2


# read image, define the path 'feekra'
image_path = os.path.join('.', 'data', 'bird.jpg')
# calling the path
img = cv2.imread(image_path)
# write image means can save duplicate images 

cv2.imwrite(os.path.join('.', 'data', 'bird_copy.jpg'), img)

# visualize image
cv2.imshow('image', img)
cv2.waitKey(0)


