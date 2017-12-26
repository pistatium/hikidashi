# coding: utf-8

from flask import current_app, Blueprint, jsonify, Response
import requests

from hikidashi.settings import SWAGGER_UI_HOST


api = Blueprint('api', __name__)


@api.route('/', defaults={'path': ''})
@api.route('/<path:path>')
def index(path):
    if SWAGGER_UI_HOST:
        res = requests.get(f'{SWAGGER_UI_HOST}/{path}')
        return Response(res.content, content_type=res.headers['content-type'])
    return jsonify({})


@api.route('/health')
def health():
    return jsonify({'status': 'ok'})


@api.route('/items')
def list_items():
    return jsonify({
        'items': [i.to_dict() for i in g.store.get_items()]
    })


@api.route('/items/<key>', methods=['GET'])
def get_item(key):
    item = g.store.get_item(key)
    if not item:
        return jsonify({'error': 'item not found.'}), 404
    return jsonify(item.to_dict())


@api.route('/items/<key>', methods=['PUT'])
def put_item(key):
    return jsonify()
