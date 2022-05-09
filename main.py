import cv2
import numpy as np
from PIL import Image

imageTest = cv2.imread('images/DJI_0001.jpg')
resizedImg = cv2.resize(imageTest, dsize=(1600, 900), interpolation=cv2.INTER_CUBIC)

test = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2HSV)

exportImg = cv2.imwrite('filtredImages/filtredimage1.jpg', test)

cv2.imshow("nome_da_janela", test)

cv2.waitKey(0)