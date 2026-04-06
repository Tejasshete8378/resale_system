from flask import Blueprint, jsonify
from backend.models import items

items_bp = Blueprint('items_bp', __name__)

@items_bp.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)