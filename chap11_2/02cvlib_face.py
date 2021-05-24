import cv2
import cvlib as cv
import numpy as np

image = cv2.imread('images/people2.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

faces, confidences = cv.detect_face(image)

for (x,y, x2,y2), conf in zip(faces, confidences): # x2 = x+ w, y2 = y+h
    # 얼굴 roi 지정
    face_img = image[y:y2, x:x2]
    # 성별 예측하기
    label, confidence = cv.detect_gender(face_img)

    gender = np.argmax(confidence)
    text = f'{label[gender]}:{confidence[gender]:.1%}'
    cv2.putText(image, text, (x,y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
    cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)

# 영상 출력
cv2.imshow('CVlib - Face detector', image)
cv2.waitKey(0)

cv2.destroyAllWindows()