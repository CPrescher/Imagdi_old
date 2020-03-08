import io

import flask
from flask import request

import numpy as np
import fabio

app = flask.Flask(__name__)


class ImgBrowser():
    def __init__(self):
        self._filename = ''
        self.img_data = None

    def load_image(self, filename):
        self.img_data = fabio.open(filename).data

    @property
    def byte_img(self):
        bytestream = io.BytesIO()
        np.save(bytestream, self.img_data)
        return bytestream.getvalue()


browser = ImgBrowser()


@app.route('/load', methods=['POST'])
def load_image():
    filename = request.form.get('filename')
    browser.load_image(filename)
    return browser.byte_img
