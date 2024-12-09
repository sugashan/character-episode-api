from flask_smorest import Blueprint
from flask import session, jsonify
from app.models.models import User
from app.routes.v1.schema import LoginRequestSchema

auth = Blueprint('auth', __name__, description="Auth API")

@auth.route('/login', methods=['POST'])
@auth.arguments(LoginRequestSchema, location="json") 
@auth.response(200)
@auth.doc(description="Login/Create User", params={})
def login(user):
    """ Login Or Create User"""

    user = User.get_or_create(user["username"])
    session['user'] = user.username
    return jsonify({"message": "Logged in", "user": user.to_dict()})

@auth.route('/logout', methods=['POST'])
@auth.response(200)
@auth.doc(description="Logout User", params={})
def logout():
    """ Logout User"""

    session.pop('user', None)
    return jsonify({"message": "Logged out"})
