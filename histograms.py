import glob
import cv2
import matplotlib.pyplot as plt
import os.path

inputDir = 'images'
outputDir = 'outputHistograms'


if not os.path.exists(inputDir):
    os.mkdir("images")

if not os.path.exists(outputDir):
    os.mkdir("outputHistograms")

tipos_imagem = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif')  # Adicione mais tipos de imagem se necessário
arquivos_imagem = []
for tipo in tipos_imagem:
    arquivos_imagem.extend(glob.glob(os.path.join(inputDir, tipo)))

for index, arquivo in enumerate(arquivos_imagem, start=1):
    imagem = cv2.imread(arquivo)

    channels = cv2.split(imagem)
    colors = ("red", "green", "blue")

    for (channel, color) in zip(channels, colors):
        hist = cv2.calcHist([channel], [0], None, [256], [0,256])
        hist /= hist.sum()

        plt.plot(hist, color=color)
        plt.title("Histograma RGB")
        plt.xlabel("Valor Pixel")
        plt.ylabel("Frequencia")

os.chdir(outputDir)
plt.savefig("histograma_{}.png".format(index))