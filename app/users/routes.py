from flask import Blueprint, make_response, jsonify, request

from .models import db, User
from .schema import user_schema

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/', methods=['GET'])
def home():
    return "hello from users service", 200
