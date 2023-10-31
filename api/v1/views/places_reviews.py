#!/usr/bin/python3
"""a new view for Review object that handles all default RESTFul API actions"""
from api.v1.views import app_views
from models import storage
from models.place import Place
from models.review import Review
from flask import jsonify, abort, request


@app_views.route('/places/reviews', methods=['GET'], strict_slashes=False)
def get_all_reviews():
    """Retrieves the list of all Review objects of a Place"""
    query = storage.all(Review)
    reviews = [review.to_dict() for review in query.values()]
    return jsonify(reviews)


@app_views.route('/places/reviews', methods=['GET'], strict_slashes=False)
def get_review(place_id):
    """Retrieves the list of all Review objects of a Place."""
    review = storage.get(Place, place_id)
    if not place_id:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/places/reviews', methods=['GET'], strict_slashes=False)
def get_review(place_id):
    """Retrieves a Review object"""
    review = storage.get(Review, review_id)
    if not review_id:
        abort(404)
        return jsonify(review.to_dict())


@app_views.route('/places/reviews', methods=['DELETE'], strict_slashes=False)
def del_review(review_id):
    """Deletes a Review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/reviews', methods=['POST'], strict_slashes=False)
def new_review():
    """Creates a Review"""
    if not request.get_json():
        abort(400, 'Not a JSON')
    if not place_id:
        abort(404)
    if 'user_id' not in request.get_json():
        abort(400, 'Missing user_id')
    if not user_id:
        abort(404)
    if 'text' not in request.get_json():
        abort(400, 'Missing text')
    storage.new(new_review)
    storage.save()
    return jsonify(review.to_dict()), 201
