import os
import shutil
import io
import unittest
import tempfile

from PIL import Image
import numpy as np

from backend.app import app


def create_temp_tiff(img_data):
    temp_file = tempfile.NamedTemporaryFile("wb", suffix=".tiff")
    im = Image.fromarray(img_data)
    im.save(temp_file)
    return temp_file


def save_tiff(img_data, filename):
    with open(filename, "wb") as f:
        im = Image.fromarray(img_data)
        im.save(f)


def create_random_tiff_file_series(img_arrays):
    temp_directory_path = os.path.join(tempfile.gettempdir(), 'imagdi')
    os.mkdir(temp_directory_path)
    file_names = []
    for ind, img_array in enumerate(img_arrays):
        file_name = os.path.join(temp_directory_path, 'series_{:03d}.tiff'.format(ind + 1))
        save_tiff(img_array, file_name)
        file_names.append(file_name)
    return file_names


class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        shutil.rmtree(os.path.join(tempfile.gettempdir(), 'imagdi'), ignore_errors=True)

    def test_load_image(self):
        rand_img = np.random.random((5, 5))
        temp_file = create_temp_tiff(rand_img)

        response = self.app.post('/load', data=dict(filename=temp_file.name))
        self.assertEqual(response.status_code, 200)
        received_img = np.load(io.BytesIO(response.data))

        self.assertTrue(np.allclose(received_img, rand_img))
        self.assertEqual(rand_img.shape, received_img.shape)

    def test_load_next_image(self):
        img_arrays = [np.random.random((5, 5)) for _ in range(10)]
        file_names = create_random_tiff_file_series(img_arrays)

        # load first image
        response = self.app.post('/load', data=dict(filename=file_names[0]))
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/next')
        self.assertEqual(response.status_code, 200)

        received_img = np.load(io.BytesIO(response.data))
        self.assertTrue(np.allclose(received_img, img_arrays[1]))
        self.assertEqual(img_arrays[1].shape, received_img.shape)

    def test_load_previous_image(self):
        img_arrays = [np.random.random((5, 5)) for _ in range(3)]
        file_names = create_random_tiff_file_series(img_arrays)

        # load third image
        response = self.app.post('/load', data=dict(filename=file_names[2]))
        self.assertEqual(response.status_code, 200)

        response = self.app.post('/previous')
        self.assertEqual(response.status_code, 200)

        received_img = np.load(io.BytesIO(response.data))
        self.assertTrue(np.allclose(received_img, img_arrays[1]))
        self.assertEqual(img_arrays[1].shape, received_img.shape)

    def test_get_filename(self):
        temp_file = create_temp_tiff(np.random.random((5, 5)))

        response = self.app.post('/load', data=dict(filename=temp_file.name))
        self.assertEqual(response.status_code, 200)

        response = self.app.get('/filename')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), str(temp_file.name))


