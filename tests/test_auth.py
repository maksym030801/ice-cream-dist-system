import unittest
from flask import json
from app import create_app, db
from app.models import User


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test variables. This method is called before each test."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        # Create the database and the database table
        db.create_all()

        # Define user data
        self.user_data = {
            'username': 'user1',
            'password': '12341234'
        }

    def tearDown(self):
        """Teardown all initialized variables."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_login(self):
        """Test API can login a user (POST request)"""
        res = self.client.post('/auth/login', data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(res.status_code, 200)
        # Additional assertions can include checking the response data, such as a token

if __name__ == '__main__':
    unittest.main()
