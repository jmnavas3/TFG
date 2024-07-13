from flask import Blueprint


api_route = Blueprint('api', __name__)

@api_route.route('', methods=['GET'])
def index():
    return "Hola Mundo!", 200
