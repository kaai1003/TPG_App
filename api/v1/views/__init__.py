#!/usr/bin/python3
"""api views init module"""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.user import *
from api.v1.views.login import *
from api.v1.views.suppliers import *
from api.v1.views.connectors import *
from api.v1.views.testprobes import *
from api.v1.views.testmodules import *
