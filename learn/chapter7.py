# color detection
import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)

        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def empty(_):
    pass

path = '../resource/car.png'

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue min", "TrackBars", 14, 179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sat max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val max", "TrackBars", 255, 255, empty)

# sua thanh mau HSV
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue max", "TrackBars")
    sat_min = cv2.getTrackbarPos("Sat min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Sat max", "TrackBars")
    val_min = cv2.getTrackbarPos("Val min", "TrackBars")
    val_max = cv2.getTrackbarPos("Val max", "TrackBars")

    print(h_min, h_max, sat_min, sat_max, val_min, val_max)
    lower = np.array([h_min, sat_min, val_min])
    upper = np.array([h_min, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask, )

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stack images", imgStack)
    cv2.waitKey(1)

