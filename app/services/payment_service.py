import time
from random import choice

def process_payment(order_id, amount):
    """
    Simulates payment processing.
    This function would actually call an external payment gateway API in a real application.
    """
    # Simulate a delay to mimic interaction with a slow payment gateway
    time.sleep(choice([60, 120, 180]))  # Random delay between 1 to 3 seconds
    # Simulate different payment outcomes
    return choice(['succeeded', 'failed'])
