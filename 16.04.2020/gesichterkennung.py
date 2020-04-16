import cv2 as cv
import numpy
import matplotlib.pyplot as plt

img = cv.imread("img2.jpg")

img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

classifier = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
faces = classifier.detectMultiScale(img_gray)
print(faces)

for x,y,w,h in faces:
    cv.rectangle(img,(x,y),(w+x,h+y),(0,0,255), 2)

img_RGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.imshow(img_RGB)
plt.show()