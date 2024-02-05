import unittest
from flask import json
from app import create_app, db
from app.models import Order, User

class OrderTestCase(unittest.TestCase):
    def setUp(self):
        # Configure your application for testing
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        # Optionally, add a test user here if your order creation depends on having a user in the db
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_order(self):
        # Assuming your create order endpoint expects a user_id, flavor_id, and quantity in the JSON body
        # Here's an example payload. Adjust according to your actual model
        data = {
            'user_id': 1,  # Make sure this user exists in your test db
            'flavor_id': 1,  # Adjust accordingly
            'quantity': 3
        }
        response = self.client.post('/orders/create_order', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        # Further assertions can include checking the response data or querying the db to ensure the order was created
        # For example:
        self.assertIn('Order created and payment processing started', response.get_data(as_text=True))
        # Query the database to ensure the order was created
        order = Order.query.first()
        self.assertIsNotNone(order)
        self.assertEqual(order.user_id, data['user_id'])

if __name__ == '__main__':
    unittest.main()
