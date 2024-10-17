#!/usr/bin/python3
"""testmodules views module"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.testmodules import TestModule


@app_views.route('/testmodules', methods=['GET'],
                 strict_slashes=False)
def get_testmodules():
    """retrieve all testmodules"""
    all_testmodules = storage.all(TestModule)
    list_testmodules = []
    for obj in all_testmodules.values():
        list_testmodules.append(obj.to_dict())
    return jsonify(list_testmodules), 200


@app_views.route('/testmodules/<testmodule_id>', methods=['GET'],
                 strict_slashes=False)
def get_testmodule(testmodule_id):
    """retrive testmodule based on id"""
    list_testmodules = storage.all(TestModule)
    for obj in list_testmodules.values():
        if obj.id == testmodule_id:
            return jsonify(obj.to_dict()), 200
    abort(404)


@app_views.route('/testmodules/<supplier_id>', methods=['GET'],
                 strict_slashes=False)
def get_tm_of_supplier(supplier_id):
    """retrive testmodule based on id"""
    all_testmodules = storage.all(TestModule)
    list_testmodules = []
    for obj in all_testmodules.values():
        if obj.supplier_id == supplier_id:
            list_testmodules.append(obj.to_dict())
    return jsonify(list_testmodules), 200


@app_views.route('/testmodules/<testmodule_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_testmodule(testmodule_id):
    """delete testmodule"""
    all_testmodules = storage.all(TestModule)
    for obj in all_testmodules.values():
        if obj.id == testmodule_id:
            storage.delete(obj)
            storage.save()
            return jsonify({'message': 'testmodule deleted...'}), 200
    abort(404)


@app_views.route('/testmodules', methods=['POST'],
                 strict_slashes=False)
def add_testmodule():
    """create new testmodule"""
    if request.is_json:
        dict = request.get_json()
        print(dict)
        if "serial_number" not in dict.keys():
            abort(400, "Missing testmodule serial_number")
        if "terminals" not in dict.keys():
            abort(400, "Missing testmodule terminals")
        if "pushback" not in dict.keys():
            abort(400, "Missing pushback status")
        if "supplier_id" not in dict.keys():
            abort(400, "Missing testmodule supplier id")
        if "connector_id" not in dict.keys():
            abort(400, "Missing testmodule connector id")
        if "probeid" not in dict.keys():
            abort(400, "Missing testmodule testprobe id")
        new_tm = TestModule(**dict)
        storage.new(new_tm)
        storage.save()
        return jsonify(new_tm.to_dict()), 201
    abort(400, "Not a JSON")


@app_views.route('/testmodules/<testmodule_id>', methods=['PUT'],
                 strict_slashes=False)
def update_testmodule(testmodule_id):
    """update testmodule"""
    testmodule = storage.get(TestModule, testmodule_id)
    if testmodule is not None:
        if request.is_json:
            inputs = request.get_json()
            for key, value in inputs.items():
                ignore = ['id', 'serial_number', 'created_at', 'updated_at']
                if key not in ignore:
                    setattr(testmodule, key, value)
            testmodule.save()
            return jsonify(testmodule.to_dict()), 200
        abort(400, "Not a JSON")
    abort(404)
