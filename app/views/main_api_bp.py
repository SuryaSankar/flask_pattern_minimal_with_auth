from flask import Blueprint, jsonify

main_api_bp = Blueprint('main_api_bp', __name__)


@main_api_bp.route("/")
def index():
    return jsonify({
            "status": "success"
        })
