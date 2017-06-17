import unittest
from flask_testing import TestCase
import os
import tempfile
from src.main import create_app, db


class BaseTestCase(unittest.TestCase):
    def create_app(self):
        return create_app("settings/test.py")

    def setUp(self):
        self.app = self.create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
