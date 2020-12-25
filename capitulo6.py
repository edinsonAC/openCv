import cv2
import numpy as np

img = cv2.imread('resources/nach.jpg')

#hor = np.hstack((img,img))
#ver = np.vstack((img,img))

#cv2.imshow("Horizontal ", hor)
#cv2.imshow("Vertical ", ver)

cv2.waitKey(0)