import os
import unittest

from backend.app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_load_image(self):
        response = self.app.post('/load_image', data=dict(filename='blubg'))
        print(response)
