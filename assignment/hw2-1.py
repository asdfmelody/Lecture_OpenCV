import numpy as np
import cv2

def onChange1(value):
    global minPos, maxPos
    minPos=cv2.getTrackbarPos("V_min", title)
    print("minPos : ", minPos)
    th, v2 = cv2.threshold(v, minPos, maxPos, cv2.THRESH_TOZERO)
    hsv2_image=cv2.merge([h,s,v2])
    color_image=cv2.cvtColor(hsv2_image,cv2.COLOR_HSV2BGR)
    cv2.imshow(title, color_image)
def onChange2(value):
    global maxPos
    maxPos=cv2.getTrackbarPos("V_max", title)
    print("maxPos : ", maxPos)
    th, v2 = cv2.threshold(v, maxPos, 255, cv2.THRESH_TOZERO_INV)
    hsv2_image=cv2.merge([h,s,v2])
    color_image=cv2.cvtColor(hsv2_image,cv2.COLOR_HSV2BGR)
    cv2.imshow(title, color_image)


image = cv2.imread("flowers.jpg", cv2.IMREAD_COLOR)

title = "HW 2-1"

cv2.imshow(title, image)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv_image)

cv2.createTrackbar("V_min", title, 0,255, onChange1)
cv2.setTrackbarPos("V_min", title, 100)

cv2.createTrackbar("V_max", title, 0,255, onChange2)
cv2.setTrackbarPos("V_max", title, 255)

cv2.waitKey(0)
cv2.destroyAllWindows()