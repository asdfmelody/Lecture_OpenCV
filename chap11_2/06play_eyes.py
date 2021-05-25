import numpy as np
import cv2
from Common.haar_utils import *

face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt2.xml")  # 정면 검출기
if face_cascade.empty(): raise IOError('Unable to load the face cascade classifier xml file')
eye_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_eye.xml")  # 눈 검출기
if eye_cascade.empty(): raise IOError('Unable to load the eye cascade classifier xml file')

image = cv2.imread('images/people2.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

# 선글라스 영상
sunglasses_img = cv2.imread('./images/sunglass2.png')
if sunglasses_img is None: raise Exception("선글라스 영상 파일 읽기 에러")

img_gray = preprocessing(image)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 2, 0, (100, 100))  # 얼굴 검출

for x, y, w, h in faces : # face in faces :
 #   x, y, w, h = face
    face_image = img_gray[y:y + h, x:x + w]  # 얼굴 영역 영상 가져오기
    eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))  # 눈 검출 수행
    eye_centers = []
    if len(eyes) == 2 :
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(image, (x + ex, y + ey, ew, eh), (0, 0, 255), 2)
            eye_centers.append((x + ex+int(ew*0.5), y + ey+int(eh*0.5)))
            cv2.circle(image, (x + ex+int(ew*0.5), y + ey+int(eh*0.5)), 3, (0, 180, 255), 2)
            # 실습
        # 실습
        sunglasses_width = 2.34 * abs(eye_centers[1][0] - eye_centers[0][0])
        sh, sw = sunglasses_img.shape[:2]
        scaling_factor = sunglasses_width / sw
        overlay_sunglasses = cv2.resize(sunglasses_img, None, fx=scaling_factor, fy=scaling_factor,
                                interpolation=cv2.INTER_AREA)

        sx = eye_centers[0][0] if eye_centers[0][0] < eye_centers[1][0] else eye_centers[1][0]
        sy = eye_centers[0][1] if eye_centers[0][0] < eye_centers[1][0] else eye_centers[1][1]
        sx = int(sx - 0.26 * overlay_sunglasses.shape[1])
        sy = int(sy - 0.21 * overlay_sunglasses.shape[0])
        sh, sw = overlay_sunglasses.shape[:2]

        overlay_img = np.ones(image.shape, np.uint8) * 255
        overlay_img[sy:sy + sh, sx:sx + sw] = overlay_sunglasses
        #cv2.imshow("overlay_img", overlay_img)

        gray_sunglasses = cv2.cvtColor(overlay_img, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(gray_sunglasses, 180, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        temp = cv2.bitwise_and(image, image, mask=mask)
        temp2 = cv2.bitwise_and(overlay_img, overlay_img, mask=mask_inv)
        image = cv2.add(temp, temp2)

    else :
        print("눈 미검출")

    cv2.rectangle(image, (x,y,w,h), (255,0,0), 2) #face, (255,0,0), 2)

cv2.imshow("Eyes Detector", image)
cv2.waitKey(0)

cv2.destroyAllWindows()