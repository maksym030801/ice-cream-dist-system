import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.simulate.config import BASE_URL

# The URL of your login endpoint
LOGIN_URL = f'{BASE_URL}/auth/login'


# Function to simulate a single user login
def simulate_user_login(user_id):
    # Assuming the login requires a username and password
    login_payload = {
        'username': f'user{user_id}',
        'password': '12341234'
    }
    response = requests.post(LOGIN_URL, json=login_payload)
    if response.status_code == 200:
        return f"User {user_id} logged in successfully."
    else:
        return f"User {user_id} failed to login. Status Code: {response.status_code}"


# Number of concurrent users to simulate
NUMBER_OF_USERS = 1000 # 10000

# Using ThreadPoolExecutor to simulate concurrent logins
with ThreadPoolExecutor(max_workers=100) as executor:
    # Submit all login tasks to the executor
    future_to_user = {executor.submit(simulate_user_login, user_id): user_id for user_id in
                      range(1, NUMBER_OF_USERS + 1)}

    # Process the results as they are completed
    for future in as_completed(future_to_user):
        user_id = future_to_user[future]
        try:
            result = future.result()
            print(result)
        except Exception as exc:
            print(f'User {user_id} generated an exception: {exc}')

