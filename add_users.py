from werkzeug.security import generate_password_hash
from app import create_app
from app.models import db, User

def add_users():
    app = create_app()
    with app.app_context():
        for i in range(1, 1001):  # 1 to 1000
            username = f"user{i}"
            password_hash = generate_password_hash('12341234')
            user = User(username=username, password_hash=password_hash)
            db.session.add(user)

        db.session.commit()
        print("1,000 users have been added to the database.")

if __name__ == '__main__':
    add_users()
