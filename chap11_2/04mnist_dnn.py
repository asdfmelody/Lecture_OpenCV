import cv2, numpy as np
import gzip

# python으로 배우는 OpenCV 프로그래밍
# OpenCV 3 Computer Vision with Python Cookbook

# 실습

#net = cv2.dnn.readNetFromTensorflow('./dnn/MINIST_MLP_frozen_graph.pb')
net = cv2.dnn.readNetFromTensorflow('./dnn/MINIST_CNN_frozen_graph2.pb')

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(dst, (x, y), 10, (255, 255, 255), -1)
    cv2.imshow('dst', dst)


dst = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
cv2.imshow('dst', dst)
cv2.setMouseCallback('dst', onMouse)

mode = cv2.RETR_EXTERNAL
method = cv2.CHAIN_APPROX_SIMPLE
font = cv2.FONT_HERSHEY_SIMPLEX
x_img = np.zeros(shape=(28, 28), dtype=np.uint8)  # 입력이미지(28*28)


while True:
    key = cv2.waitKey(25)
    if key == 27:
        break;
    elif key == ord('r'):  # ord 함수는 문자의 유니코드 값을 돌려주는 함수
        dst[:, :] = 0
        cv2.imshow('dst', dst)
    elif key == ord(' '):
        gray = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        contours, _ = cv2.findContours(gray, mode, method)
        for i, cnt in enumerate(contours):
            x, y, width, height = cv2.boundingRect(cnt)
            cv2.rectangle(dst, (x, y), (x + width, y + height), (0, 0, 255), 2)
            cx, cy = x + width / 2, y + height / 2
            if width > height:  # 큰 변 길이
                r = width / 2
            else:
                r = height / 2
            cx, cy, r = int(cx), int(cy), int(r)
            img = gray[cy - r:cy + r, cx - r:cx + r]  # 정사각형 이미지
            img = cv2.resize(img, dsize=(20, 20), interpolation=cv2.INTER_AREA)
            x_img[:, :] = 0
            x_img[4:24, 4:24] = img  # 입력이미지에 숫자 넣기
            x_img = cv2.dilate(x_img, None, 2)
            x_img = cv2.erode(x_img, None, 4)
            cv2.imshow('x_img', x_img)

            # 실습
            #x_test = np.float32(x_img.flatten())  # 2차원 영상을 1차원 배열로
            #_, res, _, _ = knn.findNearest(x_test.reshape(-1, 784), k=1)

            blob = cv2.dnn.blobFromImage(x_img)  # blob.shape=(1, 1, 28, 28)
            net.setInput(blob)
            res = net.forward()
            y_predict = np.argmax(res, axis=1)
            cv2.putText(dst, str(int(y_predict)), (x, y), font, 3, (255, 0, 0), 5)

        cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

