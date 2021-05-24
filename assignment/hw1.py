#20181007 최희선

import numpy as np
import cv2

def onChange(value):		# 트랙바 콜백 함수
    global image, title                     	# 전역 변수 참조

    r = cv2.getTrackbarPos(bar_red, title)  #빨간색 설정
    g = cv2.getTrackbarPos(bar_green, title)    #green 설정
    b = cv2.getTrackbarPos(bar_blue, title)     #blue 설정

    image[:] = [b, g, r]    #image에 적용

    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):
    global title, pt                            # 전역 변수 참조

    if event == cv2.EVENT_LBUTTONDOWN:      #왼쪽 마우스 클릭

        if flags & cv2.EVENT_FLAG_SHIFTKEY:  #직선

            if pt[0] < 0:
                pt = (x, y)
                cv2.imshow(title, image)
            else:
                cv2.line(image,pt,(x,y),(0,255,0),2)    #직선 그리기
                cv2.imshow(title, image)
                pt = (-1, -1)                       # 시작 좌표 초기화

        if flags & cv2.EVENT_FLAG_ALTKEY:  #사각형
            if pt[0] < 0:
                pt = (x, y)
                cv2.imshow(title, image)
            else:
                cv2.rectangle(image, pt, (x, y), (255,0,0), 2)  #사각형 그리기
                cv2.imshow(title, image)
                pt = (-1, -1)                       # 시작 좌표 초기화

        elif flags & cv2.EVENT_FLAG_CTRLKEY:    #원
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(image, pt, 1, 0, 2)  # 타원의 중심점(2화소 원) 표시
                cv2.imshow(title, image)
            else:
                dx, dy = pt[0] - x, pt[1] - y  # 두 좌표 간의 거리
                radius = int(np.sqrt(dx * dx + dy * dy))    #반지름
                cv2.circle(image, pt, radius, (0, 0, 255), 2)   #원그리기
                cv2.imshow(title, image)
                pt = (-1, -1)  # 시작 좌표 초기화

    if event == cv2.EVENT_RBUTTONDOWN:  #색 채우기

        if flags & cv2.EVENT_FLAG_ALTKEY:  #사각형
            if pt[0] < 0:
                pt = (x, y)
                cv2.imshow(title, image)
            else:
                cv2.rectangle(image, pt, (x, y), orange, -1)    #오렌지 색으로 색채우기(-1)
                cv2.imshow(title, image)
                pt = (-1, -1)                       # 시작 좌표 초기화

        elif flags & cv2.EVENT_FLAG_CTRLKEY:    #원
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(image, pt, 1, 0, 2)  # 타원의 중심점(2화소 원) 표시
                cv2.imshow(title, image)
            else:
                dx, dy = pt[0] - x, pt[1] - y  # 두 좌표 간의 거리
                radius = int(np.sqrt(dx * dx + dy * dy))    #반지름
                cv2.circle(image, pt, radius, cyan, -1)     #민트색으로 색채우기 (-1)
                cv2.imshow(title, image)
                pt = (-1, -1)  # 시작 좌표 초기화


image = np.zeros((300, 500,3), np.uint8)           	# 영상 생성

title = 'HW Event'
cv2.imshow(title, image)

bar_red = "Red"
cv2.createTrackbar(bar_red, title, 0, 255, onChange)	# 트랙바 콜백 함수 등록

bar_green = "Green"
cv2.createTrackbar(bar_green, title, 0, 255, onChange)	# 트랙바 콜백 함수 등록

bar_blue = "Blue"
cv2.createTrackbar(bar_blue, title, 0, 255, onChange)	# 트랙바 콜백 함수 등록

olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
orange, cyan = (0, 165, 255), (255, 255, 0)

pt = (-1, -1)                                   # 시작 좌표 초기화

cv2.imshow(title, image)                        # 윈도우에 영상 띄우기
cv2.setMouseCallback(title, onMouse)            # 마우스 콜백 함수 등록

cv2.waitKey(0)
cv2.destroyAllWindows()
