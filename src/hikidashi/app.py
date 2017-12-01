# coding: utf-8

from flask import Flask, jsonify
from flask import Response
import requests

from hikidashi.settings import SWAGGER_UI_HOST


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    if SWAGGER_UI_HOST:
        res = requests.get(f'{SWAGGER_UI_HOST}/{path}')
        return Response(res.content, content_type=res.headers['content-type'])
    return jsonify({})


@app.route('/health')
def health():
    return jsonify({'status': 200})


@app.route('/items')
def list_items():
    return jsonify()


@app.route('/items/<key>', methods=['GET'])
def get_item(key):
    return jsonify()


@app.route('/items/<key>', methods=['PUT'])
def put_item(key):
    return jsonify()
