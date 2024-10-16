#!/usr/bin/python3
"""connectors views module"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.connectors import Connector


@app_views.route('/connectors', methods=['GET'],
                 strict_slashes=False)
def get_connectors():
    """retrieve all connectors"""
    all_connectors = storage.all(Connector)
    list_connectors = []
    for obj in all_connectors.values():
        list_connectors.append(obj.to_dict())
    return jsonify(list_connectors), 200


@app_views.route('/connectors/<connector_id>', methods=['GET'],
                 strict_slashes=False)
def get_connector(connector_id):
    """retrive connector based on id"""
    all_connector = storage.all(Connector)
    for obj in all_connector.values():
        if obj.id == connector_id:
            return jsonify(obj.to_dict()), 200
    abort(404)


@app_views.route('/connectors/<supplier_id>', methods=['GET'],
                 strict_slashes=False)
def get_connectors_of_supplier(supplier_id):
    """retrive connector based on id"""
    all_connector = storage.all(Connector)
    list_connectors = []
    for obj in all_connector.values():
        if obj.supplier_id == supplier_id:
            list_connectors.append(obj.to_dict())
    return jsonify(list_connectors), 200


@app_views.route('/connectors/<connector_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_connector(connector_id):
    """delete connector"""
    all_connector = storage.all(Connector)
    for obj in all_connector.values():
        if obj.id == connector_id:
            storage.delete(obj)
            storage.save()
            return jsonify({'message': 'connector deleted...'}), 200
    abort(404)


@app_views.route('/connectors', methods=['POST'],
                 strict_slashes=False)
def add_connector():
    """create new connector"""
    if request.is_json:
        dict = request.get_json()
        if "serial_number" not in dict.keys():
            abort(400, "Missing connector")
        if "terminals" not in dict.keys():
            abort(400, "Missing password")
        if "supplier_id" not in dict.keys():
            abort(400, "Missing Role")
        new_connector = Connector(**dict)
        storage.new(new_connector)
        storage.save()
        return jsonify(new_connector.to_dict()), 201
    abort(400, "Not a JSON")


@app_views.route('/connectors/<connector_id>', methods=['PUT'],
                 strict_slashes=False)
def update_connector(connector_id):
    """update connector"""
    connector = storage.get(Connector, connector_id)
    if connector is not None:
        if request.is_json:
            inputs = request.get_json()
            for key, value in inputs.items():
                ignore = ['id', 'created_at', 'updated_at']
                if key not in ignore:
                    setattr(connector, key, value)
            connector.save()
            return jsonify(connector.to_dict()), 200
        abort(400, "Not a JSON")
    abort(404)
