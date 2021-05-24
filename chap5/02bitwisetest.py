import numpy as np, cv2

# 파이썬을 만드는 OPENCV 프로젝트
image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)  # 영상 읽기
image_mask = np.zeros_like(image)
#numpy.zeros(배열, dtype=자료형)을 사용하여 모든 원소의 값이 0인 배열을 생성
#numpy.zeros_like(배열, dtype=자료형)을 사용하여 배열의 크기와 동일하며 모든 원소의 값이 0인 배열을 생성

h, w = image.shape[:2]
cx,cy  = w//2, h//2
cv2.circle(image_mask, (cx,cy), 100, (255,255,255), -1)      		# 중심에 원 그리기

image4 = cv2.bitwise_and(image, image_mask)    	# 원소 간 논리곱

cv2.imshow("image1", image);			cv2.imshow("image2", image_mask)
cv2.imshow("bitwise_and", image4)

cv2.waitKey(0)