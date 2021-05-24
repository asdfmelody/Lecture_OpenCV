import cv2
import numpy as np

# 이미지를 읽어서 그레이 스케일 및 스레시홀드 변환
img = cv2.imread("images/shapes.png")
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

# 컨투어 찾기
contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(th,contours, -1, (155,0,0), 3)
cv2.imshow('dst4', th)
print(len(contours))

for contour in contours:
    # 각 컨투어에 근사 컨투어로 단순화
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    vertices = len(approx)

    mmt = cv2.moments(contour)
    cx, cy = int(mmt['m10'] / mmt['m00']), int(mmt['m01'] / mmt['m00'])

    name = "Unkown"
    color = (255, 255, 255)
    if vertices == 3:  # 꼭지점이 3개는 삼각형
        name = "Triangle"
        color = (255, 0, 0)
    elif vertices == 4:
        x, y, w, h = cv2.boundingRect(contour)
        if abs(w - h) <= 3:
            name = 'Square'
            color = (0, 255, 0)
        else :
            name = 'Rectangle'
            color = (0, 255, 255)
    elif vertices == 10:  # 꼭지점 갯수 10개는 별
        name = 'Star'
        color = (255, 255, 0)
    elif vertices >= 15:  # 꼭지점 10개 이상이면 원
        name = 'Circle'
        color = (255, 0, 255)
    cv2.drawContours(img2, [contour], -1, color, -1)
    cv2.putText(img2, name, (cx - 50, cy), cv2.FONT_HERSHEY_COMPLEX_SMALL, \
                1, (100, 100, 100), 1)

cv2.imshow('Input Shapes', img)
cv2.imshow('Recognizing Shapes', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()