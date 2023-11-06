from flask import Blueprint

healthcheck_bp = Blueprint('healthcheck_blueprint', __name__, url_prefix="/healthcheck")

@healthcheck_bp.route('/health', methods=["GET"])
def get_healthcheck(): 
    return {
        "message": "FoodieAPI is running and healthy!"
    }