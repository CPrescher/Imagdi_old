import flask
from flask import request

app = flask.Flask(__name__)

class ImgBrowser():
    def __init__(self):
        self._filename = ''
        self.img_data = None

    def load_image(self, filename):
        self.img_data = "haha"

browser = ImgBrowser()


@app.route('/load', methods=['POST'])
def load_image():
    filename = request.args.get('filename')
    browser.load_image(filename)
    return browser.img_data
