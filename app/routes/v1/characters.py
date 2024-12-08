from flask_smorest import Blueprint
from flask import jsonify, request

from app.connector.rick_and_morty_api import fetch_characters_using_grapghQL
from app.routes.v1.schema import CharacterResponseSchema, GetCharactersQueryArgsSchema
from app.utils.cache import get_cached_data, set_cached_data

characters = Blueprint('characters', __name__, description="Character Cards API")

@characters.route('/characters', methods=['GET'])
@characters.response(200, CharacterResponseSchema(many=True))
@characters.arguments(GetCharactersQueryArgsSchema, location="query")
@characters.doc(description="Get All Characters.")
def get_characters(parameters):
    """Get All Characters"""
    
    page = parameters["page"]

    cached_characters = get_cached_data('characters', page)
    if not cached_characters:
        characters = fetch_characters_using_grapghQL(page)
        set_cached_data('characters', characters, page)
    else:
        characters = cached_characters

    return jsonify(characters), 200
