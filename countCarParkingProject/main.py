import cv2
import pickle
import cvzone
import numpy as np

# idea:
# store car parking positions and cut it
# change them to bit images
# check in binary images
    # to convert to binary image
    # conver image to image gray => blur => threshold
# if they have many bits => car parked
# else available


# car parking width and height
width, height = 107, 48

#video feed
cap = cv2.VideoCapture('resource/carPark.mp4')

# get existing pos saved
try:
    with open('resource/CarParkPos', 'rb') as f:
        postList = pickle.load(f)
except:
    postList = []

def checkParkingSpace(imgProcess):
    freeSpaceCounter = 0
    for pos in postList:
        x, y = pos
        # crop single car parking of image binary
        imgCrop = imgProcess[y:y+height, x:x+width]
        # cv2.imshow(str(x*y), imgCrop)
        # count bits of each car parking position  => saw that if no car parked, maximum bits are approximately 900
        count = cv2.countNonZero(imgCrop)
        maxCountBitsOfPosNoCarParked = 900
        if count < maxCountBitsOfPosNoCarParked:
            color = (0, 255, 0)
            thickness = 5
            freeSpaceCounter+=1
        else:
            color = (0, 0, 255)
            thickness = 2

        # draw rectangle
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness)
        # draw bits of each car parking
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1, thickness=2, offset=0, colorR=(0, 0, 255))

    cvzone.putTextRect(img, f'Free: {freeSpaceCounter}/{len(postList)}', (100, 50), scale=3, thickness=5, offset = 20, colorR=(0, 255, 0))


while True:
    # reset frame to loop video forever
    # current frame                       # total frame
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    # remove noise bit
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    # make the line weighter
    kernel = np.ones((3,3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    # checking car parking space
    checkParkingSpace(imgDilate)

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break