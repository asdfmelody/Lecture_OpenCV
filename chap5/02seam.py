import numpy as np, cv2

# 파이썬으로 만드는 OpenCV 프로젝트
# 적절한 알파와 베타값을 찾지 않고 합성 : seamlessClone
#cv2.seamlessClone(src, dst, mask, center_position, 합성방식)

# --① 합성 대상 영상 읽기
img1 = cv2.imread("images/drawing.jpg")
img2 = cv2.imread("images/my_hand.jpg")
cv2.imshow('drawing', img1); cv2.imshow('my_hand', img2)

# --② 마스크 생성, 합성할 이미지 전체 영역을 255로 셋팅
mask = np.full_like(img1, 255)

# --③ 합성 대상 좌표 계산(img2의 중앙)
height, width = img2.shape[:2]
center = (width // 2, height // 2)

# --④ seamlessClone 으로 합성
normal = cv2.seamlessClone(img1, img2, mask, center, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(img1, img2, mask, center, cv2.MIXED_CLONE)

# --⑤ 결과 출력
cv2.imshow('normal', normal)
cv2.imshow('mixed', mixed)

cv2.waitKey()
cv2.destroyAllWindows()