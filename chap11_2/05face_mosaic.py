import numpy as np, cv2
from Common.haar_utils import *


face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt2.xml")  # 정면 검출기
if face_cascade.empty(): raise IOError('Unable to load the face cascade classifier xml file')


cap = cv2.VideoCapture('images/KBS-Special-2011-10-09.mp4')
fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)


while True:
    ret, frame = cap.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    img_gray = preprocessing(frame)

    faces = face_cascade.detectMultiScale(img_gray, 1.1, 2, 0, (100, 100))  # 얼굴 검출

    for x, y, w, h in faces:  # face in faces :
        #   x, y, w, h = face
        face_image = frame[y:y + h, x:x + w]  # 얼굴 영역 영상 가져오기

        # 실습
        #roi = cv2.bilateralFilter(face_image, 31, 80, 80)
        roi = cv2.resize(face_image, (w // 15, h // 15))
        roi = cv2.resize(roi, (w, h), interpolation=cv2.INTER_AREA)
        frame[y:y + h, x:x + w] = roi

        cv2.rectangle(frame, (x, y, w, h), (255, 0, 0), 2)  # face, (255,0,0), 2)

    cv2.imshow("Face Detector", frame)

cap.release()