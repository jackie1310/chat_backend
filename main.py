from flask import Flask, request
from flask_cors import CORS
from predict import classify_img

app = Flask(__name__)
CORS(app)

@app.route('/classify', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('img_url')
    result = classify_img(message)
    return {'result': result}

@app.route('/', methods=["GET"])
def say_hello():
    return "Hello Helios"

if __name__ == '__main__':
    app.run(debug=True)