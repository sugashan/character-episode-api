from flask_smorest import Blueprint
from flask import request, jsonify, session
from app.models.models import Favorite

favorites = Blueprint('favorites', __name__, description="Favorites API")


@favorites.route('/favorites/<int:character_id>', methods=['POST'])
@favorites.response(202)
@favorites.doc(description="Add To Favorite Characters.")
def add_favorite(character_id):
    """ Add To Favorite Characters. """
    
    print(session.get('user'))

    username = session.get('user')
    if not username:
        return jsonify({"error": "Not authenticated"}), 403

    if not character_id:
        return jsonify({"error": "Character ID is required"}), 400

    favorite = Favorite.toggle(username, character_id)
    return jsonify({"message": "Favorite status updated", "favorite": favorite})
