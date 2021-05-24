import numpy as np, cv2

# Python으로 배우는 OpenCV 프로그래밍

src1 = cv2.imread('images/book1.jpg')  # 'cup1.jpg'
src2 = cv2.imread('images/book2.jpg')  # 'cup2.jpg'
img1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

orbF = cv2.ORB_create(nfeatures=1000)  # ①
kp1, des1 = orbF.detectAndCompute(img1, None)
kp2, des2 = orbF.detectAndCompute(img2, None)

bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)  # ②
matches = bf.match(des1, des2)
#flan = cv2.FlannBasedMatcher_create()
#matches = flan.match(np.float32(des1), np.float32(des2))

matches = sorted(matches, key=lambda m: m.distance)  # 정렬
print('len(matches)=', len(matches))
for i, m in enumerate(matches[:3]):
    print('matches[{}]=(queryIdx:{}, trainIdx:{}, distance:{})'.format(
        i, m.queryIdx, m.trainIdx, m.distance))

minDist = matches[0].distance
good_matches = list(filter(lambda m: m.distance < 4*minDist, matches))
print('len : ', len(good_matches))
if(len(good_matches) < 5) :
    print("Sorry, too small good matches")
    exit()

src1_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches])
src2_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches])
H, mask = cv2.findHomography(src1_pts, src2_pts, cv2.RANSAC, 3.0)
h, w = img1.shape
pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)

pts2 = cv2.perspectiveTransform(pts, H)

src2 = cv2.polylines(src2, [np.int32(pts2)], True, (255, 0, 0), 2)

#st = cv2.drawMatches(src1, kp1, src2, kp2, matches, None, flags=0)
#cv2.imshow('dst', dst)

dst2 = cv2.drawMatches(src1,kp1,src2,kp2, good_matches, None, flags=2)
cv2.imshow('dst', dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()