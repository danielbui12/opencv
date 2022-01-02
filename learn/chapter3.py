#resize image
import cv2
import numpy as np

img = cv2.imread('../resource/test.jpg')
imgResize = cv2.resize(img,(1000, 500)) #(img, width, height)

# print(imgResize.shape) # return height width type shape

imgCropped = img[0:200, 2:500] #[height, width]
cv2.imshow("Cropped image", imgCropped)
cv2.imshow("Image", img)
cv2.imshow('Resize image', imgResize)

cv2.waitKey(0)
cv2.destroyAllWindows()