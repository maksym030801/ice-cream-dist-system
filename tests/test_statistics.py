import unittest
from flask import Flask
from your_application import create_app, db
from your_application.models import Order

class StatisticsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        # Prepopulate the database with orders for statistics
        self.populate_orders_for_statistics()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def populate_orders_for_statistics(self):
        # Add orders to the database to test statistics
        pass  # Implement your data setup for statistics here

    def test_order_statistics(self):
        response = self.client.get('/statistics')  # Adjust the endpoint as needed
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        # Assert on the expected statistical data
        # Example:
        # self.assertEqual(data['total_orders'], expected_total_orders)
        # self.assertEqual(data['most_popular_flavor'], expected_most_popular_flavor)

if __name__ == '__main__':
    unittest.main()
