import cv2
import numpy as np

src = cv2.imread('images/pixel.jpg')

hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

roi = cv2.selectROI(src)
print('roi =', roi)
roi_h = h[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
hist = cv2.calcHist([roi_h], [0], None,[60], [0, 180]) #hist[r][c] = hist[y][x]
backP= cv2.calcBackProject([hsv[:,:,0].astype(np.float32)], [0], hist, [0, 180], scale=1.0)

hist = cv2.sort(hist, cv2.SORT_EVERY_COLUMN+cv2.SORT_DESCENDING)
print(hist)
k = 1
T = hist[k][0] -1 # threshold

ret, dst = cv2.threshold(backP, T, 255, cv2.THRESH_BINARY)
cv2.imshow('dst',  dst)

color_img = cv2.bitwise_and(src, src, mask=dst.astype(np.uint8))
cv2.imshow('back', color_img)

cv2.waitKey()
cv2.destroyAllWindows()

import matplotlib.pyplot as plt
plt.ground