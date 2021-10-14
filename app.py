from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from yoga_utils.utils import decodeImage
from predict import yoga

app = Flask(__name__)
CORS(app)

# @cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = yoga(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictionyoga()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run()