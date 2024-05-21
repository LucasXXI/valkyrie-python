import glob
import cv2
import numpy as np
import os.path

inputDir = 'images'
outputDir = 'outputImagesRGB'


if not os.path.exists(inputDir):
    os.mkdir("images")

if not os.path.exists(outputDir):
    os.mkdir("outputImagesRGB")

tipos_imagem = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif')
arquivos_imagem = []
for tipo in tipos_imagem:
    arquivos_imagem.extend(glob.glob(os.path.join(inputDir, tipo)))

for index, arquivo in enumerate(arquivos_imagem, start=1):
    try:
        image = cv2.imread(arquivo)

        (blue, green, red) = cv2.split(image)

        zeros = np.zeros(image.shape[:2], dtype="uint8")
        blue = cv2.merge([blue, zeros, zeros])
        green = cv2.merge([zeros, green, zeros])
        red = cv2.merge([zeros, zeros, red])

        os.chdir(outputDir)

        cv2.imwrite(f"redRGB_{index}.png", red)
        cv2.imwrite(f"greenRGB_{index}.png", green)
        cv2.imwrite(f"blueRGB_{index}.png", blue)
    except Exception as e:
        print(f"Erro ao processar a imagem {arquivo}: {e}")