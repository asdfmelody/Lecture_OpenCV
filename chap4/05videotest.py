import cv2
from Common.utils import put_string

#capture = cv2.VideoCapture(0)  # 0번 카메라 연결
capture = cv2.VideoCapture("images/video_file2.avi")  
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

fps = 29.97                                         # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
size  = (640, 360)                                  # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'DX50')            # 압축 코덱 설정

capture.set(cv2.CAP_PROP_ZOOM, 1)                   # 카메라 속성 지정
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH , size[0])     	# 해상도 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

# 동영상 파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("images/video_test.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

frame_cnt = 0                                       	# 현재 프레임 번호

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    frame_cnt += 1

    blue, green, red = cv2.split(frame)

    if 100 <= frame_cnt < 200:
        cv2.add(blue, 100, blue)  # blue 채널 밝기 증가
    elif 200 <= frame_cnt < 300:
        cv2.add(green, 100, green)  # green 채널 밝기 증가
    elif 300 <= frame_cnt < 400:
        cv2.add(red, 100, red)  # red 채널 밝기 증가

    frame = cv2.merge([blue, green, red])  # 단일채널 영상 합성

    put_string(frame, "frame_cnt : ", (20, 320), frame_cnt)

    writer.write(frame)  # 프레임을 동영상으로 저장

    title = "View Frame from Camera"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기

capture.release()