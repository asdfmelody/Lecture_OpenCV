import cv2
import pafy

url = "https://www.youtube.com/watch?v=FJkzm6X5feY"

video = pafy.new(url)
best = video.getbest(preftype="mp4")
capture = cv2.VideoCapture(best.url)

print("video title : {}".format(video.title))  # 제목
print("video rating : {}".format(video.rating))  # 평점
print("video viewcount : {}".format(video.viewcount))  # 조회수
print("video author : {}".format(video.author))  # 저작권자
print("video length : {}".format(video.length))  # 길이
print("video duration : {}".format(video.duration))  # 길이
print("video likes : {}".format(video.likes)) # 좋아요
print("video dislikes : {}".format(video.dislikes)) #싫어요

#fourcc = cv2.VideoWriter_fourcc(*'DX50')            # 압축 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
frameWidth = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHeight = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (frameWidth, frameHeight)
fps = int(capture.get(cv2.CAP_PROP_FPS))

# 동영상 파일 개방 및 코덱, 해상도 설정
writer = cv2.VideoWriter("images/youtube_test.mp4", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    writer.write(frame)

    title2 = "View Frame from youtube"
    cv2.imshow(title2, frame)  # 윈도우에 영상 띄우기

capture.release()