from flask import Flask, jsonify, request, render_template, url_for
import base64
from pycode.py_qrcode_reader import detect_qr_code
from io import BytesIO
import os, cv2
import re
import numpy as np

app = Flask(__name__, static_url_path='/static', static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        request_data = request.get_json()
        print(request_data['imgBase64'])
        imagedata = request_data['imgBase64']
        # imagedata = base64.b64encode(imagedata)
        base64_data = re.sub('^data:image/.+;base64,', '', imagedata)
        print(base64_data)
        imgdata = BytesIO(base64.b64decode(base64_data))
        nparr = np.frombuffer(base64.b64decode(base64_data), np.uint8)
        cvimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        src_abs_path = os.path.abspath('raw.png')
        dst_abs_path = os.path.abspath('decode.png')
        cv2.imwrite(src_abs_path,cvimg)
        found, decode_data = detect_qr_code(src_abs_path,dst_abs_path)
    except Exception as e:
        print(e)
        return jsonify({'found':False,'decode_data':"{}".format(e)}), 500
    
    return jsonify({'found':found,'decode_data':decode_data}), 200
    

if __name__ == '__main__':
    app.run()