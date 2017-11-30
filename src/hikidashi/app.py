# coding: utf-8

from flask import Flask, jsonify


app = Flask(__name__)


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
