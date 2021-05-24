import numpy as np, cv2, math

def draw_houghLines(src, lines, nline):
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)  # 컬러 영상 변환
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]  # 수직거리 , 각도 - 3차원 행렬임
        # 0 .. 3.14(180)
        if ((radian > 0.1 and radian < 1.4) or (radian > 1.7 and radian < 3.)):
            a, b = math.cos(radian), math.sin(radian)
            pt = (a * rho, b * rho)  # 검출 직선상의 한 좌표 계산
            delta = (-1000 * b, 1000 * a)  # 직선상의 이동 위치
            pt1 = np.add(pt, delta).astype('int')
            pt2 = np.subtract(pt, delta).astype('int')
            cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)

    return dst

capture = cv2.VideoCapture("images/highway.avi")
if capture.isOpened() == False:
    raise Exception("동영상 연결 안됨")

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(image, (5, 5), 2, 2)
    canny = cv2.Canny(blur, 100, 200, 5)

    rho, theta = 1, np.pi / 180
    lines2 = cv2.HoughLines(canny, rho, theta, 80)
    dst2 = draw_houghLines(image, lines2, 7)
    cv2.imshow("dst2", dst2)

    title = "Lane detection"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기

capture.release()
