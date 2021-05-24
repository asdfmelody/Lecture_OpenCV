from Common.haar_utils import *
import numpy as np

def correct_image(image, face_center, eye_centers):
    pt0, pt1 = eye_centers
    if pt0[0] > pt1[0]: pt0, pt1 = pt1, pt0  # 두 좌표 스왑

    dx, dy = np.subtract(pt1, pt0).astype(float)  # 두 좌표간 차분 계산
    angle = cv2.fastAtan2(dy, dx)  # 차분으로 기울기 계산
    rot_mat = cv2.getRotationMatrix2D(face_center, angle, 1)

    size = image.shape[1::-1]  # 행태와 크기는 역순
    corr_image = cv2.warpAffine(image, rot_mat, size, cv2.INTER_CUBIC)

    eye_centers = np.expand_dims(eye_centers, axis=0)  # 차원 증가
    corr_centers = cv2.transform(eye_centers, rot_mat)
    corr_centers = np.squeeze(corr_centers, axis=0)  # 차원 감소

    return corr_image, corr_centers

face_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt2.xml")  # 정면 검출기
if face_cascade.empty(): raise IOError('Unable to load the face cascade classifier xml file')
eye_cascade = cv2.CascadeClassifier("haarcascade/haarcascade_eye.xml")  # 눈 검출기
if eye_cascade.empty(): raise IOError('Unable to load the eye cascade classifier xml file')

image = cv2.imread("images/face/34.jpg", cv2.IMREAD_COLOR)

img_gray = preprocessing(image)

faces = face_cascade.detectMultiScale(img_gray, 1.1, 2, 0, (100, 100))  # 얼굴 검출

for x, y, w, h in faces : # face in faces :
 #   x, y, w, h = face
    face_image = img_gray[y:y + h, x:x + w]  # 얼굴 영역 영상 가져오기
    eyes = eye_cascade.detectMultiScale(face_image, 1.15, 7, 0, (25, 20))  # 눈 검출 수행
    if len(eyes) == 2 :
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(image, (x+ex, y+ey, ew, eh), (0,0,255), 2)

        face_center = (x + w // 2, y + h // 2)
        eye_centers = [(x + ex + ew // 2, y + ey + eh // 2) for ex, ey, ew, eh in eyes]
        corr_image, corr_center = correct_image(image, face_center, eye_centers)  # 기울기 보정
        cv2.circle(corr_image, tuple(corr_center[0]), 5, (0, 255, 0), 2)
        cv2.circle(corr_image, tuple(corr_center[1]), 5, (0, 255, 0), 2)
        cv2.circle(corr_image, face_center, 3, (0, 0, 255), 2)
        cv2.imshow("correct_image", corr_image)
    else :
        print("눈 미검출")

    cv2.rectangle(image, (x,y,w,h), (255,0,0), 2) #face, (255,0,0), 2)

cv2.imshow("Face Detector", image)
cv2.waitKey(0)

cv2.destroyAllWindows()