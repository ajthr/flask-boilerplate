import unittest

from app import app, db
from config import settings

class AppTests(unittest.TestCase):
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

    # create more tests
