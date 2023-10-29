#!/usr/bin/python3
"""module containing a route that returns JSON"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from flask import Flask


@app_views.route('/status', strict_slashes=False)
def status():
    """returns a JSON status"""
    return jsonify({"status": "OK"})


@app_views.route('/status', strict_slashes=False)
def count():
    """an endpoint that retrieves the number of each objects by type"""
    return jsonify({"amenities": storage.count("Amenity"),
                    "cities": storage.count("City"),
                    "places": storage.count("Place"),
                    "reviews": storage.count("Review"),
                    "states": storage.count("State"),
                    "users": storage.count("User")})
