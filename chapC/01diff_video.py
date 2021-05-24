import numpy as np, cv2


def get_frame(cap):
    ret, frame = cap.read()
    if ret:
        return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    else:
        return []


def frame_diff(prev_frame, cur_frame):
    return cv2.absdiff(prev_frame, cur_frame)


cap = cv2.VideoCapture('images/roofdestory.mp4')
fps = cap.get(cv2.CAP_PROP_FPS) # 프레임 수 구하기
delay = int(1000/fps)

prev_frame = get_frame(cap)
while True:
    cur_frame = get_frame(cap)
    if cur_frame == [] : break

    diff = frame_diff(prev_frame, cur_frame)

    cv2.imshow("Motion", diff)
    prev_frame = cur_frame

    if cv2.waitKey(delay) & 0xff == 27 : break

cap.release()
