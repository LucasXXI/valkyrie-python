import json
from downloadImages import downloadImages
from main import main
from deleteFile import deleteFile


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    downloadImages(event.body.link, event.body.imageId)
    pathImage = '{}.JPG'.format(event.body.imageId)
    main(pathImage)

    response = {
        "statusCode": 200,
        "body": 'funfo'
    }

    return response

