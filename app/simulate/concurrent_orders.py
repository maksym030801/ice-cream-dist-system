import requests
import concurrent.futures
import random
from config import BASE_URL

# URL of your Flask orders endpoint
ORDERS_CREATE_ORDER_URL = f'{BASE_URL}/orders/create_order'

# Sample data for creating an ice-cream order
def generate_order_data():
    # flavors = ['vanilla', 'chocolate', 'strawberry', 'mint']
    users = [i for i in range(1, 101)]
    flavors = [1, 2, 3, 4]
    return {
        'user_id': f'user{random.choice(users)}',
        'flavor_id': random.choice(flavors),
        'quantity': random.randint(1, 100),
    }

# Function to send a POST request to create an order
def place_order(_):
    data = generate_order_data()
    response = requests.post(ORDERS_CREATE_ORDER_URL, json=data)
    return response.status_code, response.json()

# Number of concurrent orders to simulate
NUM_ORDERS = 1000

# Using ThreadPoolExecutor to send requests concurrently
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(place_order, _) for _ in range(NUM_ORDERS)]
        for future in concurrent.futures.as_completed(futures):
            try:
                status_code, response = future.result()
                print(f"Response: {status_code}, {response}")
            except Exception as e:
                print(f"Request failed: {e}")

if __name__ == "__main__":
    main()
