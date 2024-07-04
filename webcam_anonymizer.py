# feekra
import argparse
import os.path
import cv2
import mediapipe as mp
def process_image(image, face_detection):

    H, W, _ = image.shape

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

# blur faces
            image[b3:b3 + h, a3:a3 + w, :] = cv2.blur(image[b3:b3 + h, a3:a3 + w, :], (50, 50))

    return image


args = argparse.ArgumentParser()

args.add_argument("--mode", default='webcam')
args.add_argument("--filePath", default=None)

args = args.parse_args()

output_directory = './output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# detect faces
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    if args.mode in ["image"]:
        # read image
        image = cv2.imread(args.filePath)

        image = process_image(image, face_detection)

        # save image

        cv2.imwrite(os.path.join(output_directory, 'output.jpg'), image)

    elif args.mode in ['video']:

        capture = cv2.VideoCapture(args.filePath)
        ret, frame = capture.read()

        output_video = cv2.VideoWriter(os.path.join(output_directory, 'output.mp4'),
                                       cv2.VideoWriter_fourcc(*'MP4V'),
                                       25,
                                       (frame.shape[1], frame.shape[0]))
        while ret:
            frame = process_image(frame, face_detection)
            output_video.write(frame)
            ret, frame = capture.read()

        capture.release()
        output_video.release()

    elif args.mode in ['webcam']:
        capture = cv2.VideoCapture(0)
        ret, frame = capture.read()

        while ret:
            frame = process_image(frame, face_detection)

            cv2.imshow('frame', frame)
            cv2.waitKey(25)
            ret, frame = capture.read()
        capture.release()
