
#Import an Image & View it

import cv2
image = cv2.imread("./Path/To/Image.extension")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

