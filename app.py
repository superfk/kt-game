from flask import Flask, jsonify, request, render_template, url_for
import base64
from pycode.py_qrcode_reader import detect_qr_code

app = Flask(__name__, static_url_path='/static', static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        request_data = request.get_json()
        imagedata = request_data['imgBase64']
    except Exception as e:
        return jsonify({'encode_data':e}), 500
    
    return jsonify({'encode_data':imagedata}), 200
    

if __name__ == '__main__':
    app.run()