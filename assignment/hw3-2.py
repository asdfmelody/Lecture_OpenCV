import numpy as np, cv2
from Common.utils import contain_pts  # 좌표로 범위 확인 함수

def draw_rect(img):
    rois = [(p - small, small * 2) for p in pts1]
    for (x, y), (w, h) in np.int32(rois):
        roi = img[y:y + h, x:x + w]  # 좌표 사각형 범위 가져오기
        val = np.full(roi.shape, 80,
                      np.uint8)  # 컬러(3차원) 행렬 생성		cv2.add(roi, val, roi)                      			# 관심영역 밝기 증가
        cv2.add(roi, val, roi)
        cv2.rectangle(img, (x, y, w, h), (0, 255, 0), 1)
    cv2.polylines(img, [pts1.astype(int)], True, (0, 255, 0), 1)  # pts는 numpy 배열
    cv2.imshow("select rect", img)


def warp(img):
    perspect_mat = cv2.getPerspectiveTransform(pts1, pts2)
    dst = cv2.warpPerspective(img, perspect_mat, (350, 400), cv2.INTER_CUBIC)
    cv2.imshow("perspective transform", dst)
    return dst

def addLogo(src1,src2):
    rows, cols, channels = src2.shape  # 로고파일 픽셀값 저장
    roi = src1[:rows, :cols]  # 로고파일 필셀값을 관심영역(ROI)으로 저장함.

    gray = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)  # 로고파일의 색상을 그레이로 변경
    ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)  # 배경은 흰색으로, 그림을 검정색으로 변경
    mask_inv = cv2.bitwise_not(mask)

    src1_bg = cv2.bitwise_and(roi, roi, mask)  # 배경에서만 연산 = src1 배경 복사

    src2_fg = cv2.bitwise_and(src2, src2, mask_inv)  # 로고에서만 연산

    dst = cv2.bitwise_or(src1_bg, src2_fg)  # src1_bg와 src2_fg를 합성

    src1[:rows, :cols] = dst  # src1에 dst값 합성

    cv2.imshow('result', src1)

def onMouse(event, x, y, flags, param):
    global check
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, p in enumerate(pts1):
            p1, p2 = p - small, p + small  # p점에서 우상단, 좌하단 좌표생성
            # 100 : p1 = 100-12 = 88, p2 = 100+12 = 112
            if contain_pts((x, y), p1, p2): check = i

    if event == cv2.EVENT_LBUTTONUP: check = -1  # 좌표 번호 초기화

    if check >= 0:  # 좌표 사각형 선택 시
        pts1[check] = (x, y)
        draw_rect(np.copy(image))
        bg = warp(np.copy(image))
        addLogo(bg,fg)
        # bg[:100, :100] = fg  # src1에 dst값 합성
        # cv2.imshow("result",bg)

image = cv2.imread('paper.jpg')
if image is None: raise Exception("영상 파일을 읽기 에러")
duksung = cv2.imread('opencv.png')
if duksung is None: raise Exception("영상 파일을 읽기 에러")
fg = cv2.resize(duksung,(100,100))

small = np.array((12, 12))  # 좌표 사각형 크기
check = -1  # 선택 좌표 사각형 번호 초기화
pts1 = np.float32([(100, 100), (300, 100), (300, 300), (100, 300)])
# [(88~112,88~112), (288~312, 88~112)
pts2 = np.float32([(0, 0), (400, 0), (400, 350), (0, 350)])  # 목적 영상 4개 좌표                         # 목적 영상 4개 좌표

draw_rect(np.copy(image))
cv2.setMouseCallback("select rect", onMouse, 0)
cv2.waitKey(0)