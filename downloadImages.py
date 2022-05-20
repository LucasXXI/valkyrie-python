import urllib.request


def downloadImages(link, nomeImagem):
    urllib.request.urlretrieve(link, 'images/{}.JPG'.format(nomeImagem))
