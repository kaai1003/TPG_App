#!/usr/bin/python3
"""suppliers views module"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.suppliers import Supplier


@app_views.route('/suppliers', methods=['GET'],
                 strict_slashes=False)
def get_suppliers():
    """retrieve all suppliers"""
    all_suppliers = storage.all(Supplier)
    list_suppliers = []
    for obj in all_suppliers.values():
        list_suppliers.append(obj.to_dict())
    return jsonify(list_suppliers), 200


@app_views.route('/suppliers/<supplier_id>', methods=['GET'],
                 strict_slashes=False)
def get_supplier(supplier_id):
    """retrive supplier based on id"""
    all_suppliers = storage.all(Supplier)
    for obj in all_suppliers.values():
        if obj.id == supplier_id:
            return jsonify(obj.to_dict()), 200
    abort(404)


@app_views.route('/suppliers/<supplier_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_supplier(supplier_id):
    """delete supplier"""
    all_supplier = storage.all(Supplier)
    for obj in all_supplier.values():
        if obj.id == supplier_id:
            storage.delete(obj)
            storage.save()
            return jsonify({'message': 'supplier deleted...'}), 200
    abort(404)


@app_views.route('/suppliers', methods=['POST'],
                 strict_slashes=False)
def add_supplier():
    """create new supplier"""
    if request.is_json:
        dict = request.get_json()
        if "name" not in dict.keys():
            abort(400, "Missing Supplier name")
        if "type" not in dict.keys():
            abort(400, "Missing Supplier type")
        new_supplier = Supplier(**dict)
        storage.new(new_supplier)
        storage.save()
        return jsonify(new_supplier.to_dict()), 201
    abort(400, "Not a JSON")


@app_views.route('/suppliers/<supplier_id>', methods=['PUT'],
                 strict_slashes=False)
def update_supplier(supplier_id):
    """update supplier"""
    supplier = storage.get(Supplier, supplier_id)
    if supplier is not None:
        if request.is_json:
            inputs = request.get_json()
            for key, value in inputs.items():
                ignore = ['id', 'created_at', 'updated_at']
                if key not in ignore:
                    setattr(supplier, key, value)
            supplier.save()
            return jsonify(supplier.to_dict()), 200
        abort(400, "Not a JSON")
    abort(404)
