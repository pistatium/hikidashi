# coding: utf-8

from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'status': 200})
