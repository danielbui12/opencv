import cv2

# doc anh (filename, flag)
# img = cv2.imread('resource/test.jpg')

# hien thi anh (ten window, file)
#cv2.imshow("Output", img)

# delay (millisecond)
# cv2.waitKey(0)

# doc video (number:camera_port, cv2.CAP_DSHOW) => dung camera
# cap = cv2.VideoCapture("resource/vtss.mp4")
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    # cap image from video
    success, img = cap.read()
    cv2.imshow("Video", img)

    # cho bam key q thi thoat
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

