import numpy as np, cv2
import os

path = '.\\images\\stitch_images\\'
images = []

for root, directories, files in os.walk(path):
    for file in files:
        if '.jpg' in file:
            img_input = cv2.imread(os.path.join(root, file))
            images.append(img_input)

# Python으로 배우는 OpenCV 프로그래밍

stitcher = cv2.Stitcher.create()
status, dst = stitcher.stitch(images)

if status != cv2.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    exit(-1)

#cv2.imshow('dst', dst)

src1 = cv2.imread('images/stitch_images/stitch_image1.jpg')
src2 = cv2.imread('images/stitch_images/stitch_image2.jpg')
src3 = cv2.imread('images/stitch_images/stitch_image3.jpg')
src4 = cv2.imread('images/stitch_images/stitch_image4.jpg')

status, dst2 = stitcher.stitch((src1, src2))
status, dst3 = stitcher.stitch((dst2, src3))
status, dst4 = stitcher.stitch((dst3, src4))

cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.imshow('dst4',  dst4)

cv2.imwrite('images/stitch_out.jpg', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()