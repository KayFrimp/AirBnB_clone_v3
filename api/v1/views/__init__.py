#!/usr/bin/python3
"""Blueprint Module for app_views"""

from flask import Blueprint
from api.v1.views.index import *
from api.v1.views.states import *

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
