import numpy as np, cv2

#파이썬으로 만드는 OpenCV 프로젝트

# 배경 제거(background subtraction)

cap = cv2.VideoCapture('images/walking.avi')
fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)

# 배경 제거 객체 생성 --- ①
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    fgmask = fgbg.apply(frame)

    cv2.imshow('frame',fgmask)
    
    if cv2.waitKey(delay) & 0xff == 27 : break

cap.release()