#!/usr/bin/python3
"""A new view for Place objects that handles all default RESTFul API actions"""
from api.v1.views import app_views
from models import storage
from models.city import City
from flask import jsonify, abort


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def get_all_places(city_id):
    """API fetches all Places objects in database"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = [place.to_dict() for place in city.places]
    return jsonify(places)
