import numpy as np
import cv2

def onChange(value):		# 트랙바 콜백 함수
    global image, title                     	# 전역 변수 참조

    r = cv2.getTrackbarPos(bar_red, title)
    g = cv2.getTrackbarPos(bar_green, title)
    b = cv2.getTrackbarPos(bar_blue, title)

    image[:] = [b, g, r]

    cv2.imshow(title, image)

image = np.zeros((300, 500,3), np.uint8)           	# 영상 생성

title = 'Trackbar Event'
cv2.imshow(title, image)

bar_red = "Red"
cv2.createTrackbar(bar_red, title, 0, 255, onChange)	# 트랙바 콜백 함수 등록

bar_green = "Green"
cv2.createTrackbar(bar_green, title, 0, 255, onChange)	# 트랙바 콜백 함수 등록

bar_blue = "Blue"
cv2.createTrackbar(bar_blue, title, 0, 255, onChange)	# 트랙바 콜백 함수 등록



cv2.waitKey(0)
cv2.destroyAllWindows()
