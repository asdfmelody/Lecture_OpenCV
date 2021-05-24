import numpy as np, cv2

# 파이썬으로 만드는 OpenCV 프로젝트
img1 = cv2.imread("images/man_face.jpg")
img2 = cv2.imread("images/skull.jpg")

cv2.imshow('man_face', img1); cv2.imshow('skull', img2)

# --② 합성할 이미지 생성
img3 = np.zeros_like(img1)
# --③ 합성 대상 좌표 계산(img2의 중앙)
height, width = img3.shape[:2]
middle = width // 2

# 입력 영상의 절반씩 복사해서 결과 영상에 합성
img3[:, :middle, : ] = img1[:, :middle, :].copy()
img3[:, middle:, :] = img2[:, middle:, :].copy()
cv2.imshow('half', img3)

start = middle - 50

# 알파 값을 바꾸면서 알파 블렌딩 적용
for i in range(101):
    alpha = (100 - i) / 100  # 증감 간격에 따른 알파 값 (1~0)
    beta = 1 - alpha  # 베타 값 (0~1)
    # 알파 블렌딩 적용
    img3[:, start + i] = img1[:, start + i] * alpha + img2[:, start + i] * beta
cv2.imshow('half skull', img3)

cv2.waitKey()
cv2.destroyAllWindows()