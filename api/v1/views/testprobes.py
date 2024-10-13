#!/usr/bin/python3
"""testprobes views module"""
from api.v1.views import app_views
from flask import jsonify
from flask import abort
from flask import request
from models import storage
from models.testprobes import TestProbe


@app_views.route('/testprobes', methods=['GET'],
                 strict_slashes=False)
def get_testprobes():
    """retrieve all testprobes"""
    all_testprobes = storage.all(TestProbe)
    list_testprobes = []
    for obj in all_testprobes.values():
        list_testprobes.append(obj.to_dict())
    return jsonify(list_testprobes), 200


@app_views.route('/testprobes/<testprobe_id>', methods=['GET'],
                 strict_slashes=False)
def get_testprobe(testprobe_id):
    """retrive testprobe based on id"""
    list_testprobes = storage.all(TestProbe)
    for obj in list_testprobes.values():
        if obj.id == testprobe_id:
            return jsonify(obj.to_dict()), 200
    abort(404)


@app_views.route('/testprobes/<supplier_id>', methods=['GET'],
                 strict_slashes=False)
def get_tp_of_supplier(supplier_id):
    """retrive testprobe based on id"""
    list_testprobes = storage.all(TestProbe)
    list_testprobes = []
    for obj in list_testprobes.values():
        if obj.supplier_id == supplier_id:
            list_testprobes.append(obj.to_dict())
    return jsonify(list_testprobes), 200


@app_views.route('/testprobes/<testprobe_id>', methods=['DELETE'],
                 strict_slashes=False)
def del_testprobe(testprobe_id):
    """delete testprobe"""
    list_testprobes = storage.all(TestProbe)
    for obj in list_testprobes.values():
        if obj.id == testprobe_id:
            storage.delete(obj)
            storage.save()
            return jsonify({'message': 'testprobe deleted...'}), 200
    abort(404)


@app_views.route('/testprobes', methods=['POST'],
                 strict_slashes=False)
def add_testprobe():
    """create new testprobe"""
    if request.is_json:
        dict = request.get_json()
        if "testprobe" not in dict.keys():
            abort(400, "Missing testprobe")
        if "password" not in dict.keys():
            abort(400, "Missing password")
        if "role" not in dict.keys():
            abort(400, "Missing Role")
        new_user = TestProbe(**dict)
        storage.new(new_user)
        storage.save()
        return jsonify(new_user.to_dict()), 201
    abort(400, "Not a JSON")


@app_views.route('/testprobes/<testprobe_id>', methods=['PUT'],
                 strict_slashes=False)
def update_testprobe(testprobe_id):
    """update testprobe"""
    testprobe = storage.get(TestProbe, testprobe_id)
    if testprobe is not None:
        if request.is_json:
            inputs = request.get_json()
            for key, value in inputs.items():
                ignore = ['id', 'testprobe', 'created_at', 'updated_at']
                if key not in ignore:
                    setattr(testprobe, key, value)
            testprobe.save()
            return jsonify(testprobe.to_dict()), 200
        abort(400, "Not a JSON")
    abort(404)
