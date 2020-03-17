from flask import Flask, jsonify, request, render_template, url_for
import base64
from pycode.py_qrcode_reader import detect_qr_code
from PIL import Image
from io import BytesIO

app = Flask(__name__, static_url_path='/static', static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    try:
        request_data = request.get_json()
        print(request_data['imgBase64'])
        imagedata = request_data['imgBase64'][22:]
        print(imagedata)
        # imagedata = base64.b64encode(imagedata)
        im = Image.open(BytesIO(base64.b64decode(imagedata)))
        im.save('rawimg.png', 'PNG')
        found, decode_data = detect_qr_code("rawimg.png","output.png")
    except Exception as e:
        print(e)
        return jsonify({'found':False,'encode_data':"{}".format(e)}), 500
    
    return jsonify({'found':found,'encode_data':decode_data}), 200
    

if __name__ == '__main__':
    app.run()