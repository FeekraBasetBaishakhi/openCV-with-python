import os
import cv2

# read video 'feekra'
video_path = os.path.join('', 'data', 'camel.mp4')

video = cv2.VideoCapture(video_path)

# visualize video

ret = True
while ret:
    ret, frame = video.read()
    if ret:
        cv2.imshow('frame', frame)
        cv2.waitKey(40)

# have to write it down after every video
video.release()
cv2.destroyAllWindows()