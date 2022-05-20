import os.path

def jsonWritter(imageData):
    if (os.path.isfile('imageData.json')):
        string_json = ""
        with open('imageData.json', "r") as arq:
            json = arq.read()
            string_json = "{},\n{}".format(json, imageData)


        with open('imageData.json', "w") as arq:
            arq.write(string_json)

    else:
        with open('imageData.json', "w") as arq:
            string_json = "{}".format(imageData)
            arq.write(string_json)