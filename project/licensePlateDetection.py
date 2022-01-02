import cv2
import pytesseract

licensePlatesCascade = cv2.CascadeClassifier('../resource/haarcascades/haarcascade_russian_plate_number.xml')
minArea = 500
color = (255, 0, 0)
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

while True:
    # cap image from video
    count = 0
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    licensePlates = licensePlatesCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in licensePlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "License plates", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        imgRoi = img[y:y+h, x:x+w] # cut bsx
        cv2.imshow("Roi", imgRoi)

    cv2.imshow("result", img)

    # cho bam key q thi thoat
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print(pytesseract.image_to_string(imgRoi))
        cv2.imwrite("../resource/Scanned/LP"+str(count)+".jpg", imgRoi)
        cv2.rectangle(img, (0, 100), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Scan saved", (150, 265), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count+=1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()