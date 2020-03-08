import io

import flask
from flask import request

import numpy as np
import fabio

from .util.FileIteration import get_next_file, get_previous_file

app = flask.Flask(__name__)


class ImgBrowser:
    def __init__(self):
        self._filename = ''
        self._fabio = None
        self.img_data = None

    def load_image(self, filename):
        self._filename = filename
        self._fabio = fabio.open(filename)
        self.img_data = self._fabio.data

    def next(self):
        if self._filename == '':
            return
        next_file_name = get_next_file(self._filename)
        self.load_image(next_file_name)

    def previous(self):
        if self._filename == '':
            return
        previous_file_name = get_previous_file(self._filename)
        self.load_image(previous_file_name)

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


@app.route('/next', methods=['POST'])
def next_file():
    browser.next()
    return browser.byte_img


@app.route('/previous', methods=['POST'])
def previous_file():
    browser.previous()
    return browser.byte_img
