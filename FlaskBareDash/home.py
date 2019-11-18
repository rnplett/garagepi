from flask import Flask
from flask import request
from io import BytesIO
from time import sleep
from picamera import PiCamera
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World!!!'

@app.route('/view')
def view():
    s = BytesIO()
    c.capture(s,'png')
    enc = base64.b64encode(s.getvalue()).decode("ascii")
    p1 = "<img src=\"data:image/png;base64,"
    p2 = "\"><br>This is what it looks like"
    t = p1 + enc + p2
    return t

if __name__ == '__main__':
    c = PiCamera()
    c.resolution = (640,320)
    c.start_preview()
    app.run(host='garagepi.local', port=5000)
