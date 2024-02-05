from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    # Relationships
    orders = db.relationship('Order', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'

class IceCreamFlavor(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f'<IceCreamFlavor {self.name}>'

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flavor_id = db.Column(db.Integer, db.ForeignKey('ice_cream_flavor.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='pending')  # e.g., pending, paid, completed

    # Relationships
    flavor = db.relationship('IceCreamFlavor')

    def __repr__(self):
        return f'<Order {self.id} by User {self.user_id}>'

# Optionally, you could include a Payment model to track payment transactions
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True,  autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., processing, succeeded, failed
    transaction_id = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f'<Payment {self.transaction_id} for Order {self.order_id}>'
