# coding: utf-8

from flask import Flask
from flask import g

from hikidashi.backends.store import Backends


def create_app(backend_name, **backend_conf):
    app = Flask(__name__)
    store = Backends.get_store(backend=backend_name, **backend_conf)

    with app.app_context():
        g.store = store

    from hikidashi.views import api
    app.register_blueprint(api)

    return app
