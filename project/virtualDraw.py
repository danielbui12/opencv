import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

listColors = [
    [5, 107, 0, 19, 255, 255],
    [133, 56, 0, 159, 156, 255],
    [57, 76, 0, 100, 255, 255],
    [82, 148, 119, 112, 148, 255]
]

listColorsValues = [
    [255, 106, 0],
    [255, 0, 255],
    [0, 255, 0],
    [0, 0, 255]
]

myPoints = [] # x, y, colorID

def findColor(img, myColors, myColorsValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    counter = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorsValue[counter], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, counter])
        counter+=1
        # cv2.imshow(str(color[0]), mask)
    return newPoints

def getContours(img):
    contours, hierarchu = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(myPoints, myColorsValue):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorsValue[point[2]], cv2.FILLED)


while True:
    # cap image from video
    success, img = cap.read()
    imgResult =  img.copy()
    newPoints = findColor(img, listColors, listColorsValues)
    if len(newPoints) != 0:
        for newPoint in newPoints:
            myPoints.append(newPoint)
    if len(myPoints) != 0:
        drawOnCanvas(myPoints, listColorsValues)

    cv2.imshow("Result", imgResult)

    # cho bam key q thi thoat
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()