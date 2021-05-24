import numpy as np, cv2

# 파이썬으로 만드는 OpenCV 프로젝트

cap = cv2.VideoCapture('images/walking.avi')
fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)

color = np.random.randint(0,255,(200,3)) # 추적 경로를 그리기 위한 랜덤 색상
lines = None  #추적 선을 그릴 이미지 저장 변수
prevImg = None  # 이전 프레임 저장 변수
termcriteria =  (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03) # calcOpticalFlowPyrLK 중지 요건 설정

while cap.isOpened():
    ret,frame = cap.read()
    if not ret:
        break
    img_draw = frame.copy()

    # 실습
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if prevImg is None: # 첫번째 프레임
        prevImg = gray
        lines = np.zeros_like(frame)
        prevPt = cv2.goodFeaturesToTrack(prevImg, 200, 0.01, 10)
    else : # 두번째 이후
        nextImg = gray
        nextPt, status, err = cv2.calcOpticalFlowPyrLK(prevImg, nextImg, prevPt, None, criteria=termcriteria)
        prevMv = prevPt[status == 1]
        nextMv = nextPt[status == 1]
        for i, (p, n) in enumerate(zip(prevMv, nextMv)):
            px, py = p.ravel()
            nx, ny = n.ravel()
            cv2.line(lines, (int(px), int(py)), (int(nx), int(ny)), color[i].tolist(), 2)
            cv2.circle(img_draw, (int(nx), int(ny)), 2, color[i].tolist(), -1)
        img_draw = cv2.add(img_draw, lines)
        # 다음 프레임을 위한 프레임과 코너점 이월
        prevImg = nextImg
        prevPt = nextMv.reshape(-1, 1, 2)
    cv2.imshow('OpticalFlow-LK', img_draw)
    key = cv2.waitKey(delay)
    if key == 27 : # Esc:종료
        break
    elif key == 8:
        prevImg = None

cv2.destroyAllWindows()
cap.release()