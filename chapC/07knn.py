import numpy as np, cv2

def draw_points(image, group, color):
    for p in group:
        pt = tuple(p.astype(int))
        cv2.circle(image, pt, 3, color, cv2.FILLED)

nsample = 50
traindata = np.zeros((nsample*2, 2), np.float32)  # 학습 데이터 행렬
label = np.zeros((nsample*2, 1), np.float32)   # 레이블

cv2.randn(traindata[:nsample], 150, 30)
cv2.randn(traindata[nsample:], 250, 60)
label[:nsample], label[nsample:] = 0 , 1

# 실습
knn = cv2.ml.KNearest_create()
knn.train(traindata, cv2.ml.ROW_SAMPLE, label)

K = 15
points = [(x, y) for y in range(400) for x in range(400)  ]
ret, resp, neig, dist = knn.findNearest(np.array(points, np.float32), K)

colors = [(0, 180, 0) if p==1 else  (0, 0, 180) for p in resp]

image = np.reshape(colors, (400,400,3)).astype("uint8")

draw_points(image, traindata[:nsample], color=(0, 0, 255))
draw_points(image, traindata[nsample:], color=(0, 255, 0))

cv2.imshow("sample K="+ str(K), image)

cv2.waitKey(0)