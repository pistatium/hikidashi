# coding: utf-8

from flask import Flask
from flask import g


def create_app(store):

    app = Flask(__name__)

    @app.before_request
    def set_context():
        g.store = store

    from hikidashi.views import api
    app.register_blueprint(api)

    return app
