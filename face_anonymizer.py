# feekra
import os
import cv2
import mediapipe as mp

output_directory = './output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# read image
img_path = './data/lubna.jpg'

image = cv2.imread(img_path)

H, W, _ = image.shape


# detect faces
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            a3, b3, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            a3 = int(a3 * W)
            b3 = int(b3 * H)
            w = int(w * W)
            h = int(h * H)
            # image = cv2.rectangle(image, (a3,b3), (a3 + w, b3 +h), (0,255,0), 10)
# blur faces
        # image = cv2.blur(img, (10, 10))
            image[b3:b3 + h, a3:a3 + w, :] = cv2.blur(image[b3:b3 + h, a3:a3 + w, :], (30, 30))

# save image

cv2.imwrite(os.path.join(output_directory, 'output.jpg'), image)
