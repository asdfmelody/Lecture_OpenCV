import cv2
import numpy as np


src = cv2.imread('images/jumok.jpg')

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
lowerb = (0, 60, 0)
upperb = (20, 255, 255)
bImage = cv2.inRange(hsv, lowerb, upperb) # 특정 영역을 추출, 범위 내는 255, 그 외는 0으로
cv2.imshow('bImage',  bImage)

mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(bImage, mode, method)

dst = src.copy()
cnt = contours[0]
cv2.drawContours(dst, [cnt], 0, (255,0,0), 2)
cv2.imshow('dst', dst)

hull = cv2.convexHull(cnt, returnPoints=False)
hull_points = cnt[hull[:,0]]
dst2 = dst.copy()
cv2.drawContours(dst2, [hull_points], 0, (0,255,0), 2)
#cv2.imshow('dst2',  dst2)

hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
T = 5
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    dist = d / 256
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    if dist > T :
        cv2.circle(dst2, start, 5, [0, 255, 255], -1)
        cv2.circle(dst2, end, 5, [0, 128, 255], -1)
        cv2.circle(dst2, far, 5, [0, 0, 255], -1)

        cv2.line(dst2, start, end, [255, 255, 0], 2)
        cv2.line(dst2, start, far, [0, 255, 0], 1)
        cv2.line(dst2, end, far, [0, 255, 0], 1)
cv2.imshow('dst2',  dst2)


cv2.waitKey()
cv2.destroyAllWindows()