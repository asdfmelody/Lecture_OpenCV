import numpy as np, cv2

image = cv2.imread("images/bit_test.jpg", cv2.IMREAD_COLOR)     # 원본 영상 읽기
logo  = cv2.imread("images/logo.jpg", cv2.IMREAD_COLOR)         # 로고 영상 읽기
if image is None or logo is None: raise Exception("영상 파일 읽기 오류 ")

amasks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]  # 로고 영상 이진화
cv2.imshow("masks", amasks)
masks = cv2.split(amasks)
cv2.imshow("masks-b", masks[0])
cv2.imshow("masks-g", masks[1])
cv2.imshow("masks-r", masks[2])

cv2.waitKey()