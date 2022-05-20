import os.path
def imagePath():
    imagensContagem = 0
    dir = "images"
    for path in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, path)):
            imagensContagem += 1

    return imagensContagem