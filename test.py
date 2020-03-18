from flask import Flask, jsonify, request, render_template, url_for
import base64
from pycode.py_qrcode_reader import detect_zbar
from PIL import Image
from io import BytesIO
import os
import re
from imageio import imread
import cv2
import numpy as np

base64_data = 'iVBORw0KGgoAAAANSUhEUgAAAGMAAABjAQMAAAC19SzWAAAABlBMVEX///8AAABVwtN+AAAA40lEQVQ4jdXTsQ2DMBAF0B+5oCMjsIY7r0QWCLCAWSmd17DEAqRzgXz5CZaSBh9tXCBeY/87n4F/WVeR0RnvJGtqYcZmWS1/NLnF22W04k9oTrKelBh/RjBz6PI32aFYH7P8VHuozyHx/m3boVrHnknmV9M1MEXnG/SqkhHBEPZDaoJDa3ljUHVha9E9056lqkfssTERVCUzJQxisqoQAV5ayVKTdByBWUqWit4Nttye2RXxbqfAMSwdrIjz4vkCEKGKc92wviWf0Jy2m5QTNL2noFXF92e3QaKqfa4nPgJN/7Fep6RX/Kb/sgcAAAAASUVORK5CYII='

imgdata = BytesIO(base64.b64decode(base64_data))
nparr = np.fromstring(base64.b64decode(base64_data), np.uint8)
cvimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
src_abs_path = os.path.abspath('raw.png')
dst_abs_path = os.path.abspath('decode.png')
cv2.imwrite(src_abs_path,cvimg)
found, decode_data = detect_zbar(src_abs_path,dst_abs_path)