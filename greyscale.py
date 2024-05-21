import glob
import os
import cv2

inputDir = 'images'
outputDir = 'outputImagesGrayScale'

if not os.path.exists(inputDir):
    os.mkdir("images")

if not os.path.exists(outputDir):
    os.mkdir("outputImagesGrayScale")

tipos_imagem = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif')
arquivos_imagem = []
for tipo in tipos_imagem:
    arquivos_imagem.extend(glob.glob(os.path.join(inputDir, tipo)))

for index, arquivo in enumerate(arquivos_imagem, start=1):
    try:
        image = cv2.imread(arquivo)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        os.chdir(outputDir)
        cv2.imwrite(f"grayscale_{index}.png", gray_image)
    except Exception as e:
        print(f"Erro ao processar a imagem {arquivo}: {e}")