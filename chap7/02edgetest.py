import numpy as np, cv2

image = cv2.imread("images/edge.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

data1 = [-1, 0, 0,
         0, 1, 0,
         0, 0, 0]
data2 = [0, 0, -1,
         0, 1, 0,
         0, 0, 0]
data1 = [-1, 0, 1,                         # 프리윗 수직 마스크
         -1, 0, 1,
         -1, 0, 1]
data2 = [-1,-1,-1,                         # 프리윗 수평 마스크
          0, 0, 0,
          1, 1, 1]
data1 = [-1, 0, 1,                  # 수직 마스크
         -2, 0, 2,
         -1, 0, 1]
data2 = [-1,-2,-1,                 # 수평 마스크
          0, 0, 0,
          1, 2, 1]

data1 = [-2, -1, 0,                  # 대각선 마스크
         -1, 0, 1,
         0, 1, 2]
data2 = [0,-1,-2,                 # 역대각선 마스크
          1, 0, -1,
          2, 1, 0]
data1 = [	[0,		1,		0],  	# 4 방향 필터
			[1, 	-4,		1],
			[0, 	1,		0]]
data2 = [	[-1,	-1,		-1],	# 8 방향 필터
			[-1, 	8, 	    -1],
			[-1, 	-1, 	-1]]

data1 = [	[1,		0,		0],  	# 엠보싱
			[0, 	0,		0],
			[0, 	0,		-1]]

mask1 = np.array(data1, np.float32).reshape(3, 3)
mask2 = np.array(data2, np.float32).reshape(3, 3)

dst1 = cv2.filter2D(image, -1, mask1)  # 회선 수행 및 두 방향의 크기 계산
dst2 = cv2.filter2D(image, -1, mask2)

#dst = cv2.Laplacian(image, -1, 1)      # OpenCV 라플라시안 수행 함수

#dst1 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)
#dst2 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)
#dst = cv2.add(dst1, dst2)                # 회선 결과인 두 행렬의 크기 계산

dst = cv2.add(dst1, dst2)                # 회선 결과인 두 행렬의 크기 계산
#Magnitude , Max 사용 가능

dst1, dst2 = np.abs(dst1), np.abs(dst2)  # 회선 결과 행렬 양수 변경
dst = np.clip(dst, 0, 255).astype("uint8")
dst1 = np.clip(dst1, 0, 255).astype("uint8")
dst2 = np.clip(dst2, 0, 255).astype("uint8")

cv2.imshow("image", image)
cv2.imshow("edges", dst)
cv2.imshow("dst2", dst2)
cv2.waitKey(0)