import imageFilter
import colorId
import jsonWritter
import geotag


def main(pathImage):
    coords = geotag.geotag(pathImage)
    pathFilteredImage = imageFilter.imageFilter(pathImage)
    imageData = colorId.colorId(pathFilteredImage, pathImage, coords)
    jsonWritter.jsonWritter(imageData)

#main('DJI_0001')