import cv2
import pickle

width, height = 107, 48
try:
    with open('resource/CarParkPos', 'rb') as f:
        postList = pickle.load(f)
except:
    postList = []

def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        postList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,  pos in enumerate(postList):
            x1, y1 = pos
            if x1 < x < x1+width and y1 < y < y1+height:
                postList.pop(i )
    with open('resource/CarParkPos', 'wb') as f:
        pickle.dump(postList, f)
while True:
    img = cv2.imread('resource/carParkImg.png')
    for pos in postList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 2)

    cv2.imshow('Image', img)
    cv2.setMouseCallback("Image", mouseClick)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break