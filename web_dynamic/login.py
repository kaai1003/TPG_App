#!/usr/bin/python3
""" Starts a Flask Web Application """
from models import storage
from models.users import User
from models.connectors import Connector
from models.suppliers import Supplier
from models.testmodules import TestModule
from models.testprobes import TestProbe
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def login():
    """ login page serve! """
    return render_template('login.html')

@app.route('/main/<user_id>', strict_slashes=False)
def main(user_id):
    """ main page serve! """
    all_users = storage.all(User)
    for obj in all_users.values():
        if obj.id == user_id:
            return render_template('main.html')
    return render_template('login.html')

@app.route('/main/connectors', strict_slashes=False)
def connectors():
    """ connectors page serve! """
    headers = ['ID', 'serial_number', 'terminals', 'supplier_id', 'Actions']
    all_connectors = storage.all(Connector)
    connectors = []
    for obj in all_connectors.values():
        connectors.append(obj.to_dict())
    tbtitle = 'Connectors'
    forms = ['serial_number', 'terminals', 'supplier_id', 'photo']
    return render_template('connectors.html',
                           headers=headers,
                           items=connectors,
                           tbtitle=tbtitle,
                           forms=forms)

@app.route('/main/TestProbes', strict_slashes=False)
def testprobes():
    """ testprobes page serve! """
    headers = ['ID', 'serial_number', 'stock_location', 'pushback', 'supplier_id', 'Actions']
    all_testprobes = storage.all(TestProbe)
    testprobes = []
    for obj in all_testprobes.values():
        testprobes.append(obj.to_dict())
    tbtitle = 'TestProbes'
    forms = ['serial_number', 'stock_location', 'pushback', 'supplier_id']
    return render_template('testprobes.html',
                           headers=headers,
                           items=testprobes,
                           tbtitle=tbtitle,
                           forms=forms)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001)
