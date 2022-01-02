import cv2
import numpy as np

img = cv2.imread('../resource/test.jpg')
kernel = np.ones((5, 5), np.int8) # tao ma tran 5x5 unsign integer

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
imgCanny = cv2.Canny(img, 100, 100)
# ve cac vien trang xung quanh cac vien canny (cannyImg, ma tran, line weight)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


# cv2.imshow("Gray img", imgGray)
# cv2.imshow("Blur img", imgBlur)
# cv2.imshow("Canny img", imgCanny)
cv2.imshow("Dialation img", imgDialation)
cv2.imshow("Eroded img", imgEroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

#25:55