import os
import cv2

# read webcam
webcam = cv2.VideoCapture(0)

# visualize webcam 'feekra'

while True:
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(50) & 0xFF == ord('y'):
        break
webcam.release()
cv2.destroyAllWindows()

