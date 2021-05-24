import cv2
from Common.haar_utils import *

face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt2.xml")  # 정면 검출기
if face_cascade.empty(): raise IOError('Unable to load the face cascade classifier xml file')
eye_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_eye.xml")  # 눈 검출기
if eye_cascade.empty(): raise IOError('Unable to load the eye cascade classifier xml file')
mouth_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_mcs_mouth.xml') # 입 검출기
if mouth_cascade.empty(): raise IOError('Unable to load the mouth cascade classifier xml file')

image = cv2.imread('images/people2.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

img_gray = preprocessing(image)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 2, 0, (100, 100))  # 얼굴 검출

for x, y, w, h in faces : # face in faces :
 #   x, y, w, h = face
    face_image = img_gray[y:y + h, x:x + w]  # 얼굴 영역 영상 가져오기
    eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))  # 눈 검출 수행
    if len(eyes) == 2 :
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(image, (x+ex, y+ey, ew, eh), (0,0,255), 2)
    else :
        print("눈 미검출")

    mouths = mouth_cascade.detectMultiScale(face_image, 1.7, 11)  # 입 검출 수행
    for mouth in mouths:
        mx, my, mw, mh = mouth
        cv2.rectangle(image, (x + mx, y + my, mw, mh), (0, 255, 0), 2)

    cv2.rectangle(image, (x,y,w,h), (255,0,0), 2) #face, (255,0,0), 2)

cv2.imshow("Face Detector", image)
cv2.waitKey(0)

cv2.destroyAllWindows()