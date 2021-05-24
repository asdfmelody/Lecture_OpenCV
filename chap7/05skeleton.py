import cv2
import numpy as np

# [출처] Python으로 배우는 OpenCV 프로그래밍(김동근 저)

src = cv2.imread('images/horse.png', cv2.IMREAD_GRAYSCALE)
ret, A = cv2.threshold(src, 128, 255, cv2.THRESH_BINARY)

skel_dst = np.zeros(src.shape, np.uint8)

shape1 = cv2.MORPH_CROSS
shape2 = cv2.MORPH_RECT
shape3 = cv2.MORPH_ELLIPSE
B= cv2.getStructuringElement(shape=shape2, ksize=(3,3))

done = True
while done:
    src_erode  = cv2.erode(A, B)
    cv2.imshow('erode', src_erode)
    #opening = cv2.morphologyEx(src_erode, cv2.MORPH_OPEN, B) # 불필요한 흰색 잡음 없애기, 얇은 흰색 줄 없애기
    #tmp = cv2.subtract(src_erode, opening)  # TOPHAT
    tmp = cv2.morphologyEx(src_erode, cv2.MORPH_TOPHAT, B)  # TOPHAT
    skel_dst = cv2.bitwise_or(skel_dst, tmp)
    A = src_erode.copy()
    done = cv2.countNonZero(A) != 0

    cv2.imshow('skeleton', skel_dst)

    c = cv2.waitKey(0)
    if c == 27 : # ESC
        break