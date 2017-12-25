# coding: utf-8

from flask import Flask, jsonify
from flask import Response
from flask import g
import requests

from hikidashi.settings import SWAGGER_UI_HOST, BACKEND_NAME, BACKEND_CONF
from hikidashi.backends.store import Backends


def create_app(backend_name=BACKEND_NAME, backend_conf=BACKEND_CONF):
    app = Flask(__name__)
    store = Backends.get_store(backend=BACKEND_NAME, **BACKEND_CONF)
    g.store = store


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if SWAGGER_UI_HOST:
        res = requests.get(f'{SWAGGER_UI_HOST}/{path}')
        return Response(res.content, content_type=res.headers['content-type'])
    return jsonify({})


@app.route('/health')
def health():
    return jsonify({'status': 'ok'})


@app.route('/items')
def list_items():
    return jsonify({
        'items': [i.to_dict() for i in g.store.get_items()]
    })


@app.route('/items/<key>', methods=['GET'])
def get_item(key):
    item = g.store.get_item(key)
    if not item:
        return jsonify({'error': 'item not found.'}), 404
    return jsonify(item.to_dict())


@app.route('/items/<key>', methods=['PUT'])
def put_item(key):
    return jsonify()
