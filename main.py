import cv2
import numpy as np
from PIL import Image

imageTest = cv2.imread('images/DJI_0001.jpg')
resizedImg = cv2.resize(imageTest, dsize=(1600, 900), interpolation=cv2.INTER_CUBIC)

test = cv2.cvtColor(resizedImg, cv2.COLOR_BGR2HSV)

exportImg = cv2.imwrite('filtredImages/filtredimage1.jpg', test)

cv2.imshow("nome_da_janela", test)

cv2.waitKey(0)

img = Image.open('filtredImages/filtredimage1.jpg')
numpydata = np.asarray(img)
colorGreen = 0
total = 0

for line in numpydata:
    for column in line:
        Red = column[0]
        Green = column[1]
        Blue = column[2]
        if Green > Red and Green > Blue:
            colorGreen = colorGreen +1
        total = total + 1
print(colorGreen/total)