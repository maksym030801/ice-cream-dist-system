from flask import Blueprint, request, jsonify
from flask import current_app as app
from app.models import db, Order
from app.services import process_payment
import threading
import random
import time

orders_bp = Blueprint('orders', __name__, url_prefix='/orders')

@orders_bp.route('/create_order', methods=['POST'])
def create_order():
    data = request.get_json()
    user_id = data.get('user_id')
    flavor_id = data.get('flavor_id')
    quantity = data.get('quantity')

    # Create a new order record
    new_order = Order(user_id=user_id, flavor_id=flavor_id, quantity=quantity, status='pending')
    db.session.add(new_order)
    db.session.commit()

    # Process payment asynchronously
    payment_thread = threading.Thread(target=process_payment, args=(new_order.id,))
    payment_thread.start()

    return jsonify({'message': 'Order created and payment processing started', 'order_id': new_order.id}), 201


@orders_bp.route('/', methods=['GET'])
def get_orders():
    """
    Retrieve a list of all ice-cream orders. we need to update this for search later.
    For now, this returns all orders.
    """
    try:
        orders = Order.query.all()
        orders_data = [
            {'id': order.id, 'flavor_id': order.flavor_id, 'quantity': order.quantity}
            for order in orders
        ]
        return jsonify({'orders': orders_data}), 200
    except Exception as e:
        app.logger.error(f"Error fetching orders: {e}")
        return jsonify({'message': 'Failed to fetch orders'}), 500
