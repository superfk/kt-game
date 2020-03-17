from flask import Flask, jsonify, request, render_template, url_for
from pycode.py_qrcode_reader import detect_qr_code
import base64

app = Flask(__name__, static_url_path='/static', static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    request_data = request.get_json()
    imagedata = request_data['imgBase64']
    with open('qrcode.png', "wb") as fh:
        fh.write(base64.decode(imagedata))
    found, decode_data = detect_qr_code('qrcode.png', 'qrcode_output.png')
    return decode_data
    

if __name__ == '__main__':
    app.run()