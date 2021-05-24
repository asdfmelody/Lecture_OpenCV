import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global title, pt                            # 전역 변수 참조

    if event == cv2.EVENT_LBUTTONDOWN:

        if flags & cv2.EVENT_FLAG_SHIFTKEY:  #직선

            if pt[0] < 0:
                pt = (x, y)
                cv2.imshow(title, image)
            else:
                cv2.line(image,pt,(x,y),(0,255,0),2)
                cv2.imshow(title, image)
                pt = (-1, -1)                       # 시작 좌표 초기화

        if flags & cv2.EVENT_FLAG_ALTKEY:  #사각형
            if pt[0] < 0:
                pt = (x, y)
                cv2.imshow(title, image)
            else:
                cv2.rectangle(image, pt, (x, y), (255,0,0), 2)
                cv2.imshow(title, image)
                pt = (-1, -1)                       # 시작 좌표 초기화

        elif flags & cv2.EVENT_FLAG_CTRLKEY:    #원
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(image, pt, 1, 0, 2)  # 타원의 중심점(2화소 원) 표시
                cv2.imshow(title, image)
            else:
                dx, dy = pt[0] - x, pt[1] - y  # 두 좌표 간의 거리
                radius = int(np.sqrt(dx * dx + dy * dy))
                cv2.circle(image, pt, radius, (0, 0, 255), 2)
                cv2.imshow(title, image)
                pt = (-1, -1)  # 시작 좌표 초기화

    if event == cv2.EVENT_RBUTTONDOWN:

        if flags & cv2.EVENT_FLAG_ALTKEY:  #사각형
            if pt[0] < 0:
                pt = (x, y)
                cv2.imshow(title, image)
            else:
                cv2.rectangle(image, pt, (x, y), orange, -1)
                cv2.imshow(title, image)
                pt = (-1, -1)                       # 시작 좌표 초기화

        elif flags & cv2.EVENT_FLAG_CTRLKEY:    #원
            if pt[0] < 0:
                pt = (x, y)
                cv2.circle(image, pt, 1, 0, 2)  # 타원의 중심점(2화소 원) 표시
                cv2.imshow(title, image)
            else:
                dx, dy = pt[0] - x, pt[1] - y  # 두 좌표 간의 거리
                radius = int(np.sqrt(dx * dx + dy * dy))
                cv2.circle(image, pt, radius, cyan, -1)
                cv2.imshow(title, image)
                pt = (-1, -1)  # 시작 좌표 초기화

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)    	# 색상 선언
olive, violet, brown = (128, 128, 0), (221, 160, 221), (42, 42, 165)
orange, cyan = (0, 165, 255), (255, 255, 0)

image = np.full((300, 500, 3), (255, 255, 255), np.uint8) # 흰색 배경 영상

pt = (-1, -1)                                   # 시작 좌표 초기화
title = "Draw Event"
cv2.imshow(title, image)                        # 윈도우에 영상 띄우기
cv2.setMouseCallback(title, onMouse)            # 마우스 콜백 함수 등록
cv2.waitKey(0)