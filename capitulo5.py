import cv2
import numpy as np

img = cv2.imread("resources/cartas.PNG")
print(img.shape)
#imgResize = cv2.resize(img,(250,350))

width,height = 250,350
pts1 = np.float32([[81,165],[217,140],[115,361],[263,327]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("imgOutput",imgOutput)
cv2.waitKey(0)

