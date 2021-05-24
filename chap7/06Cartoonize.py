import cv2

# [출처] Python 예제로 배우는 OpenCV(Prateek Joshi 저)

def cartoonize_image(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.medianBlur(img_gray, 7)

    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize=5)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    num_repetitions = 10
    sigma_color = 5
    sigma_space = 7
    size = 5
    # bilateralFilter를 반복하면 에지는 선명하면서 영상이 부드럽게 하여 카툰처럼 보임.
    for i in range(num_repetitions):
        img = cv2.bilateralFilter(img, size, sigma_color, sigma_space)

    dst = cv2.bitwise_and(img, img, mask=mask)

    return dst

if __name__ == '__main__':
   # img = cv2.imread('images/color_edge.jpg')
   # cv2.imshow('Cartoonize', cartoonize_image(img))
    cap = cv2.VideoCapture('images/KBS-Special-2011-10-09.mp4') # 영상
    while True:
        ret, frame = cap.read()
        c = cv2.waitKey(1)
        if c == 27:
            break
        cv2.imshow('Cartoonize', cartoonize_image(frame))

    cv2.waitKey(0)