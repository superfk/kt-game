from flask import Flask, jsonify, request, render_template, url_for
import base64
from pycode.py_qrcode_reader import detect_qr_code

app = Flask(__name__, static_url_path='/static', static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    request_data = request.get_json()
    imagedata = request_data['imgBase64']
    return jsonify({'encode_data':imagedata})
    

if __name__ == '__main__':
    app.run()