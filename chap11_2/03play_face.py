import cv2
from Common.haar_utils import *

face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt2.xml")  # 정면 검출기
if face_cascade.empty(): raise IOError('Unable to load the face cascade classifier xml file')

face_mask = cv2.imread('images/mask_hannibal2.png',cv2.IMREAD_COLOR)
h_mask, w_mask = face_mask.shape[:2]

cap=cv2.VideoCapture('images/mcem0_sa1.mp4')

while True:
    ret, frame = cap.read()
    img_gray = preprocessing(frame)
    faces = face_cascade.detectMultiScale(img_gray,1.3,5)

    for face in faces:
        x,y,w,h = face
        y=int(y+h * 0.4)
        h=int(h*0.7)
        frame_roi = frame[y:y+h,x:x+w]
        face_mask_small = cv2.resize(face_mask, (w,h), interpolation=cv2.INTER_AREA)
        gray_mask = cv2.cvtColor(face_mask_small, cv2.COLOR_RGB2GRAY)
        ret, mask=cv2.threshold(gray_mask, 150, 255, cv2.THRESH_BINARY_INV)
        masked_face = cv2.bitwise_and(face_mask_small, face_mask_small, mask=mask)
        mask_inv = cv2.bitwise_not(mask)
        masked_frame = cv2.bitwise_and(frame_roi, frame_roi, mask_inv)
        frame[y:y+h, x:x+w] = cv2.add(masked_face,masked_frame)

    cv2.imshow('Play with face',frame)
    c=cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()