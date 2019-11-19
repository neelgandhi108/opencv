
#Cropping

import cv2
cropped = image[10:500, 500:2000]  #image[y:y+h, x:x+w]
viewImage(cropped, "Doggo after cropping.")

#Resizing
import cv2
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
viewImage(resized, "After resizing with 20%")

#Rotating
import cv2
(h, w, d) = image.shape
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, 180, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
viewImage(rotated, "Doggo after rotation by 190 degrees")

#Grayscaling and Thresholding
import cv2
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, threshold_image = cv2.threshold(im, 127, 255, 0)
viewImage(gray_image, "Gray-scale doggo")
viewImage(threshold_image, "Black & White doggo")

#Blurring/Smoothing
import cv2
blurred = cv2.GaussianBlur(image, (51, 51), 0)
viewImage(blurred, "Blurred doggo")

#Drawing a Rectangle/Bounding Box
import cv2
output = image.copy()
cv2.rectangle(output, (2600, 800), (4100, 2400), (0, 255, 255), 10)
viewImage(output, "Doggo with a rectangle on his face") 


#Drawing a Line
import cv2
output = image.copy()
cv2.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
viewImage(output, "2 Doggos separated by a line")

#Writing on an Image
import cv2
output = image.copy()
cv2.putText(output, "We <3 Dogs", (1500, 3600),cv2.FONT_HERSHEY_SIMPLEX, 15, (30, 105, 210), 40) 
viewImage(output, "image with text")

#Face Detection
import cv2
image_path = "./Path/To/Photo.extension"
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor= 1.1,
    minNeighbors= 5,
    minSize=(10, 10)
)
faces_detected = format(len(faces)) + " faces detected!"
print(faces_detected)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
viewImage(image,faces_detected)

