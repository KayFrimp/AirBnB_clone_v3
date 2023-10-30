#!/usr/bin/python3
"""A new view for city objects that handles all default RESTFul API actions"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import city


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """Retrieves the list of all City objects of a State"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
        cities = [obj.to_dict() for obj in state.cities]
        return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """Retrieves the city with the city_id"""
    city = storage.get(City, city_id).to_dict()
    if len(city) == 0:
        abort(404)
    return jsonify(city)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def del_city(city_id):
    """delete a City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def new_city():
    """create a new city"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    attributes = request.get_json()
    city = City(**attributes)
    storage.new(city)
    storage.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """updates an existing City object"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    attributes = request.get_json()
    for key, value in attributes.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return jsonify(city.to_dict()), 200
