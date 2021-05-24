import cv2

src = cv2.imread('flowers.jpg')

# ROI 부분 속성 추출
x, y, w, h = cv2.selectROI(src)

# BGR -> YCrCb
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# crop은 사용자가 선택한 사각형 부분의 영상
crop = src_ycrcb[y:y+h, x:x+w]

channels = [1, 2]  # 0인덱스인 y 성분은 쓰지 않음. y 성분은 밝기 정보.
cr_bins = 128      # cr을 표현하는 범위. 256을 128로 단순화.
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0,256]
cb_range = [0,256]
ranges = cr_range + cb_range

# 히스토그램 생성
hist = cv2.calcHist([crop], channels, None, histSize, ranges) # 리스트 입력

# 히스토그램 스트레칭
# 히스토그램 큰 값은 너무 큰 값에 몰릴 수 있으므로 log스케일 해주기. +1을 해줘서 -1값을 0으로
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 히스토그램 역투영으로 마스크 생성
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)

# 마스크 연산
dst = cv2.copyTo(src, backproj)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()