#!/usr/bin/python3
""" Starts a Flask Web Application """
from models import storage
from models.users import User
from flask import Flask, render_template
import uuid
app = Flask(__name__)


@app.route('/login', strict_slashes=False)
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


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5001)
