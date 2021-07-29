from flask import Blueprint, jsonify

from .models import db, User
from .schema import user_schema

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/', methods=['GET'])
def user_home():
    return jsonify("Hello from users service"), 200
