from flask import Flask, jsonify, request
from werkzeug import secure_filename
import boto3
import io
from io import BytesIO
import sys 
import math

app = Flask (__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/', methods=['GET'])
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <input type=file name=myfile>
    <input type=submit>
    </form>'''

@app.route('/upload', methods=['POST'])
def upload():
    s3 = boto3.resource('s3')
    file = request.files['myfile']
    filename = secure_filename(file.filename)
    s3.Bucket('process-data-image').put_object(Key=filename, Body=request.files['myfile'])
    databasecode = 'CAR. CENTRAL KMch495-VILLA UNION-NANA'
    bucket="process-data-image"
    document = filename
    s3_connection = boto3.resource('s3')
    s3_object = s3_connection.Object(bucket, document)
    s3_response = s3_object.get()
    stream = io.BytesIO(s3_response['Body'].read())

    client = boto3.client('textract')
    response = client.detect_document_text(
        Document={'S3Object': {'Bucket':bucket, 'Name':document}})

    blocks=response['Blocks']
    print ('Detected Document Text')

    for block in blocks:
        print('Tipo: ' + block['BlockType'])
        if block['BlockType'] != 'PAGE':
            print('Detected:' +block['Text'])
            if block['Text'] == databasecode:
                return '<h1>Documento Verificado</h1>'
            else:
                return '<h1>Error Documento</h1>'


def DisplayBlockInformation(block):
    print('Id: {}'.format(block['Id']))
    if 'Text' in block:
        print(' Detectado: ' + block['Text'])
    print(' Tipo: ' + block['BlockType'])

if __name__ == '__main__':
    app.run(debug=True)