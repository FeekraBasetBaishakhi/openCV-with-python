# feekra
import cv2
from PIL import Image

from limit_color import get_limit

pink = [203, 192, 255]  # pink in BGR colorspace
capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_limit, upper_limit = get_limit(color=pink)

    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

    mask_ = Image.fromarray(mask)  # converting image to pil

    bbox = mask_.getbbox()  # whenever detected value will show

    if bbox is not None:
        a1, b1, a2, b2 = bbox

        frame = cv2.rectangle(frame, (a1, b1), (a2, b2), (0, 255, 0), 6)

    cv2.imshow('frame', frame)

    if cv2.waitKey(6) & 0xFF == ord('e'):
        break


capture.release()

cv2.destroyAllWindows()
