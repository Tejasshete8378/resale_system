from flask import Blueprint, jsonify

# Create Blueprint
items_bp = Blueprint('items', __name__)

# Minimal route
@items_bp.route('/items')
def get_items():
    return jsonify({"message": "Items route working"})