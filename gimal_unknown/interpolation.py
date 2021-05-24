import numpy as np
from Common.utils import contain

def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)                     # 목적 영상 생성
    radian = (degree/180) * np.pi                               # 회전 각도 - 라디언
    sin, cos = np.sin(radian), np.cos(radian)   # 사인, 코사인 값 미리 계산

    for i in range(img.shape[0]):                              # 목적 영상 순회 - 역방향 사상
        for j in range(img.shape[1]):
            jj, ii = np.subtract((j, i), pt)                # 중심좌표 평행이동,
            y = -jj * sin + ii * cos               # 회선 변환 수식
            x =  jj * cos + ii * sin
            x, y = np.add((x, y), pt)
            if contain((y, x), img.shape):                      # 입력 영상의 범위 확인
                dst[i, j] = bilinear_value(img, [x, y])           # 화소값 양선형 보간
    return dst

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    if y >= img.shape[0]-1: y = y - 1
    if x >= img.shape[1]-1: x = x - 1

    P1, P2, P3, P4 = np.float32(img[y:y+2,x:x+2].flatten())
    alpha, beta = pt[1] - y,  pt[0] - x                   # 거리 비율

    M1 = P1 + alpha * (P3 - P1)                      # 1차 보간
    M2 = P2 + alpha * (P4 - P2)
    P  = M1 + beta  * (M2 - M1)                     # 2차 보간
    return np.clip(P, 0, 255)                       # 화소값 saturation후 반환
