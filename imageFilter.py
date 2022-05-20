import cv2

def imageFilter(pathImage):


    imageTest = cv2.imread('images/{}.JPG'.format(pathImage))
    resizedImg = cv2.resize(imageTest, dsize=(1600, 900), interpolation=cv2.INTER_CUBIC)

    test = cv2.cvtColor(imageTest, cv2.COLOR_BGR2HSV)

    nomeImagensFiltrada = 'filtredImages/{}.jpg'.format(pathImage)
    exportImg = cv2.imwrite(nomeImagensFiltrada, test)

    return nomeImagensFiltrada
