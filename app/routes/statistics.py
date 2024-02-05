from flask import Blueprint, jsonify
from app.services.stats_service import generate_statistics

stats_bp = Blueprint('stats', __name__, url_prefix='/stats')

@stats_bp.route('/sales', methods=['GET'])
def sales_statistics():
    # Generate and return sales statistics
    stats = generate_statistics()
    return jsonify(stats), 200
