import cv2
import numpy as np

# Python으로 배우는 OpenCV 프로그래밍

src = cv2.imread('images/banana.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)
bImage = cv2.dilate(bImage, None)	##bImage = cv2.erode(bImage, None)
cv2.imshow('bImage',  bImage)	##cv2.imshow('src',  src)

mode   = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
contours, hierarchy = cv2.findContours(bImage, mode, method)
print('len(contours)=', len(contours))

maxLength = 0
k = 0
for i, cnt in enumerate(contours):
    perimeter = cv2.arcLength(cnt, closed = True)
    if perimeter> maxLength:
        maxLength = perimeter
        k = i
print('maxLength=', maxLength)
cnt = contours[k]
dst2 = src.copy()
cv2.drawContours(dst2, [cnt], 0, (255,0,0), 3)
#cv2.imshow('dst2',  dst2)

area = cv2.contourArea(cnt)
print('area=', area)

x, y, width, height = cv2.boundingRect(cnt)
dst3 = dst2.copy()
cv2.rectangle(dst3, (x, y), (x+width, y+height), (0,0,255), 2)
#cv2.imshow('dst3',  dst3)

rect = cv2.minAreaRect(cnt)
print('rect=', rect)
box = cv2.boxPoints(rect)
box = np.int32(box)
print('box=', box)
dst4 = dst2.copy()
cv2.drawContours(dst4,[box],0,(0,0,255),2)
#cv2.imshow('dst4',  dst4)

(x,y),radius = cv2.minEnclosingCircle(cnt)
dst5 = dst2.copy()
cv2.circle(dst5,(int(x),int(y)),int(radius),(0,0,255),2)
#cv2.imshow('dst5',  dst5)

dst6 = dst2.copy()
rows,cols = dst6.shape[:2]
[vx,vy,x0,y0] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
# (y - y0) = (vy / vx) * (x - x0)
# y = (x - x0) * (x - x0) + y0
y1 = int((-x0*vy/vx) + y0)          # x = 0 일 때
y2 = int(((cols-1-x0)*vy/vx)+y0)    # x = (cols-1) 일 때
cv2.line(dst6,(0,y1), (cols-1,y2),(0,0,255), 2)
#cv2.imshow('dst6',  dst6)

ellipse = cv2.fitEllipse(cnt)
dst7 = dst2.copy()
cv2.ellipse(dst7, ellipse,(0,0,255),2)
#cv2.imshow('dst7',  dst7)

poly = cv2.approxPolyDP(cnt, epsilon=35, closed=True)
dst8 = dst2.copy()
cv2.drawContours(dst8, [poly], 0, (0,0,255), 2)
#cv2.imshow('dst8',  dst8)

dst9 = dst2.copy()
for y in range(rows):
    for x in range(cols):
        if cv2.pointPolygonTest(cnt, (x, y), False) > 0:
            dst9[y,x] = (0, 255,0)
cv2.imshow('dst9', dst9)
cv2.waitKey()
cv2.destroyAllWindows()

