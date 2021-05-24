import cv2
import numpy as np
# 파이썬으로 만드는 OpenCV 프로젝트

ksize = 31              # 블러 처리에 사용할 커널 크기
win_title = 'mosaic'    # 창 제목
img = cv2.imread('images/dr_ochanomizu.jpg')    # 이미지 읽기

while True:
    x,y,w,h = cv2.selectROI(win_title, img, False) # 관심영역 선택
    if w > 0 and h > 0:         # 폭과 높이가 음수이면 드래그 방향이 옳음
        roi = img[y:y + h, x:x + w]  # 관심영역 지정
        #roi = cv2.blur(roi, (ksize, ksize), cv2.BORDER_REFLECT)  # 블러(모자이크) 처리
        #roi = cv2.boxFilter(roi, -1, (ksize, ksize))
        #mask = np.ones((ksize, ksize), dtype=np.float64) / (ksize * ksize)
        #roi = cv2.filter2D(roi, -1, mask)
        #roi = cv2.GaussianBlur(roi, (ksize, ksize), cv2.BORDER_DEFAULT)
        roi = cv2.bilateralFilter(roi, ksize, 80, 80)

        img[y:y + h, x:x + w] = roi  # 원본 이미지에 적용
        cv2.imshow(win_title, img)
    else:
        break
cv2.destroyAllWindows()