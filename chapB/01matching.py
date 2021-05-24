import numpy as np, cv2

# Python으로 배우는 OpenCV 프로그래밍

src1 = cv2.imread('images/book1.jpg')
src2 = cv2.imread('images/book2.jpg')
img1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

#orbF = cv2.ORB_create(nfeatures=1000)
#kp1, des1 = orbF.detectAndCompute(img1, None)
#kp2, des2 = orbF.detectAndCompute(img2, None)

siftF = cv2.xfeatures2d.SIFT_create()
kp1, des1 = siftF.detectAndCompute(img1, None)
kp2, des2 = siftF.detectAndCompute(img2, None)

#bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)
#bf = cv2.BFMatcher_create(cv2.NORM_L2, crossCheck=True)
#matches = bf.match(des1, des2)
flan = cv2.FlannBasedMatcher_create()
#matches = flan.match(des1, des2)
matches = flan.knnMatch(des1, des2, k=2)
print('len(matches)=', len(matches))

#matches = sorted(matches, key=lambda m: m.distance)
for i, m in enumerate(matches[:3]):
#    print('matches[{}]=(queryIdx:{}, trainIdx:{}, distance:{})'.format(
#        i, m.queryIdx, m.trainIdx, m.distance))
    for j, n in enumerate(m):
        print('matches[{}][{}]=(queryIdx:{}, trainIdx:{}, 	distance:{})'.format(
            i, j, n.queryIdx, n.trainIdx, n.distance))

#dst = cv2.drawMatches(src1, kp1, src2, kp2, matches, None, flags=0)
dst = cv2.drawMatchesKnn(src1, kp1, src2, kp2, matches, None, flags=0)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
