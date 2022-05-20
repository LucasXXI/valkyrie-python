from flask import Flask, jsonify, request
import base64
import main
import downloadImages
import deleteFile

app = Flask(__name__)

@app.route("/images", methods=["POST"])
def imageFilter():
    imageId = request.json.get("userId")
    link = request.json.get("link")
    if not imageId or not link:
        return jsonify({'error': 'Please provide userId and name'}), 400


    downloadImages.downloadImages(link)
    main(imageId)


    deleteFile.deleteFile('images/{}.JPG'.format(imageId))
    with open("yourfile.ext", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    deleteFile.deleteFile('filtredImages/{}.jpg'.format(imageId))

    with open("imageData.json", 'r') as file:
        jsonFile = file.read()
    deleteFile.deleteFile('imageData.json')
    return jsonify({
        'imageId': imageId,
        'Data': jsonFile,
        'file': encoded_string
    })
