import os
import io
import unittest
import tempfile

from PIL import Image
import numpy as np

from backend.app import app


def create_random_tiff(img_data):
    temp_file = tempfile.NamedTemporaryFile("wb", suffix=".tiff")
    im = Image.fromarray(img_data)
    im.save(temp_file)
    return temp_file


class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_load_image(self):
        rand_img = np.random.random((5, 5))
        temp_file = create_random_tiff(rand_img)

        response = self.app.post('/load', data=dict(filename=temp_file.name))
        received_img = np.load(io.BytesIO(response.data))

        self.assertTrue(np.allclose(received_img, rand_img))
        self.assertEqual(rand_img.shape, received_img.shape)

