import numpy as np, cv2

# python으로 배우는 OpenCV 프로그래밍

cap = cv2.VideoCapture('images/ball.wmv')
if (not cap.isOpened()):
     print('Error opening video')

height, width = (int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
                 int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))

roi_mask   = np.zeros((height, width), dtype=np.uint8)

term_crit = (cv2.TERM_CRITERIA_MAX_ITER+cv2.TERM_CRITERIA_EPS, 10, 1)

t = 0
ret, frame = cap.read()
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (0., 60., 32.), (180., 255., 255.))

roi = cv2.selectROI(frame)
x1, y1, w, h = roi
x2 = x1 + w
y2 = y1 + h
mask_roi = mask[y1:y2, x1:x2]
hsv_roi = hsv[y1:y2, x1:x2]

hist_roi = cv2.calcHist([hsv_roi], [0], mask_roi, [16], [0, 180])
cv2.normalize(hist_roi, hist_roi, 0, 255, cv2.NORM_MINMAX)

track_window = (x1, y1, x2 - x1, y2 - y1)

while True:
     ret, frame = cap.read()
     if not ret: break
     t+=1

     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
     mask = cv2.inRange(hsv, (0., 60., 32.), (180., 255., 255.))

     backP = cv2.calcBackProject([hsv],[0],hist_roi ,[0,180],1)
     backP &= mask
     cv2.imshow('backP', backP)

     # 실습
     #ret, track_window = cv2.meanShift(backP, track_window, term_crit)
     track_box, track_window = cv2.CamShift(backP, track_window, term_crit)
     x, y, w, h = track_window
     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
     cv2.imshow('tracking', frame)

     key = cv2.waitKey(25)
     if key == 27:
          break

if cap.isOpened(): cap.release();
cv2.destroyAllWindows()
