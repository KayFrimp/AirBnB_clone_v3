#!/usr/bin/python3
"""View Module for the Link between Place objects and Amenity objects
---All default RESTFul API actions are handled"""

from api.v1.views import app_views
from os import environ
from models import storage
from models.place import Place
from models.amenity import Amenity
from flask import abort, jsonify

STORAGE_TYPE = environ.get('HBNB_TYPE_STORAGE')


@app_views.route('/places/<place_id>/amenities',
                 methods=['GET'], strict_slashes=False)
def get_all_place_amenities(place_id):
    """API fetches all amenities in a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    if STORAGE_TYPE == 'db':
        amenities = [amenity.to_dict() for amenity in place.amenities]
    else:
        amenities = []
        for amenity_id in place.amenity_ids:
            amenity = storage.get(Amenity, amenity_id)
            amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_place_amenity(place_id, amenity_id):
    """DELETES Amenity object to a Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if STORAGE_TYPE == 'db':
        for amenity in place.amenities:
            if amenity.id == amenity_id:
                # Perform deletion
                place.amenities.remove(amenity)
                place.save()
                return jsonify({}), 200
        abort(404)
    else:
        for obj_id in place.amenity_ids:
            if obj_id == amenity_id:
                # Perform deletion
                place.amenity_ids.pop(amenity_id, None)
                place.save()
                return jsonify({}), 200
        abort(404)


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                 methods=['POST'], strict_slashes=False)
def link_amenity_to_place(place_id, amenity_id):
    """Links Amenity object to Place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    if STORAGE_TYPE == 'db':
        for amenity in place.amenities:
            if amenity.id == amenity_id:
                return jsonify(amenity.to_dict()), 201
        place.amenities.append(amenity)
    else:
        for obj_id in place.amenity_ids:
            if obj_id == amenity_id:
                return jsonify(amenity.to_dict()), 201
        place.amenity_ids.append(amenity_id)
