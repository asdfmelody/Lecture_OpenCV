import numpy as np
import cv2

image = np.zeros((200,400), np.unit8)           #행 200 열 400, 초기값 0
image[:] = 200                                  #초기값 0이었던 값 모두 200으로 변환

title1, title2 = 'Position1', 'Position2'       #윈도우 이름 생성
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)    
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)                #opencv이용시 앞의 값이 x값, 뒤 값이 y 값. -> np와 반대
cv2.moveWindow(title2, 400, 50)                 #title1은 150,150만큼 이동, title2는 x축으로 400, y축으로 50 이동