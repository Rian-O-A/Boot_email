from flask import request, jsonify, Blueprint

auth_route = Blueprint(__name__, "auth")

@auth_route.route("search", methods=["POST"])
def search():
    data = request.get_json()
    
    pass