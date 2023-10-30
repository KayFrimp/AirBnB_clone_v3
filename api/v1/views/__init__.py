#!/usr/bin/python3
"""Blueprint Module for app_views"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views is not None:
    from .index import *
    from .states import *
