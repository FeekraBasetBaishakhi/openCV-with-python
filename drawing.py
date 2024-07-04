#feekra

import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'board.jpg'))
print(img.shape)
# line
cv2.line(img, (100, 150), (300, 300), (138, 33, 173), 3)

# rectangle
cv2.rectangle(img,(150,250),(300,100),(232, 136, 111), 6)

# circle
cv2.circle(img, (250, 150), 20, (127, 201, 48), -3)

# text
cv2.putText(img, 'Feekra!!', (310,230), cv2.FONT_HERSHEY_SCRIPT_COMPLEX ,3 ,(74, 58, 46), 3)


cv2.imshow('img', img)
cv2.waitKey(0)
