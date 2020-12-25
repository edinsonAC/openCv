import cv2
import numpy as np

img = cv2.imread("resources/nach.jpg")
print(img.shape)
#cambiar de tamaño
imgResize = cv2.resize(img,(300,200))
#recortar imagen
imgCropped = img[0:200,200:500]

cv2.imshow("Image ",img)
cv2.imshow("Image resize ",imgResize)
cv2.imshow("Image cropped ",imgCropped)
cv2.waitKey(0)
