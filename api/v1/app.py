#!/usr/bin/python3
"""Flask App Module"""

from models import storage
from flask import Flask
from flask_cors import CORS
from flask import jsonify
from flask import Blueprint
from api.v1.views import app_views

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': "Not found"}), 404


if __name__ == '__main__':
    host = '0.0.0.0'
    port = '5000'
    app.run(host, port, threaded=True)
