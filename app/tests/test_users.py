import unittest

from app import app, db
from config import settings

class UsersTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_TEST_DATABASE_URI
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from flask boilerplate", response.data)

    def test_user_home(self):
        response = self.app.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Hello from users service", response.data)
