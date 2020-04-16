import cv2 as cv
import numpy
import matplotlib.pyplot as plt

img = cv.imread("img.jpg")
img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
print(img.shape)

# Helligkeit erhöhen Möglichkeit 1
neueHelligkeit = img + 100
neueHelligkeit = cv.cvtColor(neueHelligkeit,cv.COLOR_BGR2RGB)

# plt.imshow(neueHelligkeit)
# plt.show()
# Helligkeit Möglichkeit 1 ENDE

# Helligkeit erhöhen Möglichkeit 2
    # (2848, 4272, 3)
neueHelligkeit2 = numpy.zeros((2848,4272,3),dtype='uint8') + 20
cv.rectangle(img, (2290,900), (2730,1350), (0,0,255),20)
img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
neueHelligkeit2 = cv.add(img2,neueHelligkeit2)

plt.imshow(neueHelligkeit2)
plt.show()

# Helligkeit Möglichkeit 2 ENDE

# plt.imshow(img2)
# plt.show()