#!/usr/bin/python3
"""users views module"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.users import User


@app_views.route('/users', methods=['GET'],
                 strict_slashes=False)
def get_users():
    """retrieve all users"""
    all_users = storage.all(User)
    list_users = []
    for obj in all_users.values():
        list_users.append(obj.to_dict())
    return jsonify(list_users), 200


@app_views.route('/users/<user_id>', methods=['GET'],
                 strict_slashes=False)
def get_user(user_id):
    """retrive user based on id"""
    all_users = storage.all(User)
    for obj in all_users.values():
        if obj.id == user_id:
            return jsonify(obj.to_dict()), 200
    abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_user(user_id):
    """delete user"""
    all_users = storage.all(User)
    for obj in all_users.values():
        if obj.id == user_id:
            storage.delete(obj)
            storage.save()
            return jsonify({'message': 'user deleted...'}), 200
    abort(404)


@app_views.route('/users', methods=['POST'],
                 strict_slashes=False)
def add_user():
    """create new user"""
    if request.is_json:
        dict = request.get_json()
        if "user" not in dict.keys():
            abort(400, "Missing user")
        if "password" not in dict.keys():
            abort(400, "Missing password")
        if "role" not in dict.keys():
            abort(400, "Missing Role")
        new_user = User(**dict)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201
    abort(400, "Not a JSON")


@app_views.route('/users/<user_id>', methods=['PUT'],
                 strict_slashes=False)
def update_user(user_id):
    """update user"""
    user = storage.get(User, user_id)
    if user is not None:
        if request.is_json:
            inputs = request.get_json()
            for key, value in inputs.items():
                ignore = ['id', 'user', 'created_at', 'updated_at']
                if key not in ignore:
                    setattr(user, key, value)
            user.save()
            return jsonify(user.to_dict()), 200
        abort(400, "Not a JSON")
    abort(404)
