from PIL import Image
import numpy as np

def colorId(pathFiltredImage, pathImage,coords):
    img = Image.open(pathFiltredImage)
    numpydata = np.asarray(img)
    colorGreen = 0
    total = 0

    for line in numpydata:
        for column in line:
            Red = column[0]
            Green = column[1]
            Blue = column[2]
            if Green > Red and Green > Blue:
                colorGreen = colorGreen + 1
            total = total + 1

    quant_verde = colorGreen / total;


    imageData = '{"id": ' + '"{}"'.format(pathImage) + \
                ',\n"verde_quant": ' + '{}'.format(quant_verde) + \
                ',\n"latitude": ' + '{}'.format(coords[0]) + \
                ',\n"longitude": ' + '{}'.format(coords[1]) + '}'

    return(imageData)