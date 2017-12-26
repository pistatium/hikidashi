# coding: utf-8

from flask import Flask
from flask import g


def create_app(store):
    app = Flask(__name__)

    from hikidashi.views import api
    app.register_blueprint(api)

    with app.app_context():
        g.store = store
    return app
