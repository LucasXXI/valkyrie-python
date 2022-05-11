import cv2
import numpy as np
from PIL import Image
import os.path

imagensContagem = 0
dir = "images"
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        imagensContagem += 1


for imageQuant in range(0, imagensContagem):

    nomeImagens = 'images/DJI_000{}.jpg'.format(imageQuant+1)


    imageTest = cv2.imread(nomeImagens)
    resizedImg = cv2.resize(imageTest, dsize=(1600, 900), interpolation=cv2.INTER_CUBIC)


    test = cv2.cvtColor(imageTest, cv2.COLOR_BGR2HSV)

    nomeImagensFiltrada = 'filtredImages/filtredimage{}.jpg'.format(imageQuant + 1)
    exportImg = cv2.imwrite(nomeImagensFiltrada, test)

    #cv2.imshow("nome_da_janela", test)

    #cv2.waitKey(0)

    img = Image.open(nomeImagensFiltrada)
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

    quant_verde = colorGreen/total;
    print(nomeImagens,": ")
    print(colorGreen/total)

    imageData = {"id": nomeImagens,
                 "verde_quant": quant_verde}

    print(imageData)

    if (os.path.isfile('imageData.json')):
        print("Ola")
        string_json = ""
        with open('imageData.json',"r") as arq:
            json = arq.read()
            string_json = "{},\n{}".format(json, imageData)


        with open('imageData.json',"w") as arq:
            arq.write(string_json)

    else:
        with open('imageData.json', "w") as arq:
            string_json = "{}".format(imageData)
            arq.write(string_json)
