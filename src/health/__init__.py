from flask import Blueprint

health_blueprint = Blueprint('health_check', __name__)

from . import resources
