# coding: utf-8

import json
import pytest
import copy

from flask.testing import FlaskClient

from hikidashi.app import create_app
from hikidashi.models.item import Item
from hikidashi.backends.store import Backends
from hikidashi.settings import BACKEND_NAME, BACKEND_CONF


def get_test_store():
    conf = copy.deepcopy(BACKEND_CONF)
    conf['table_name'] = 'test_hikidashi'
    return Backends.get_store(BACKEND_NAME, **conf)


@pytest.fixture
def client() -> FlaskClient:
    store = get_test_store()
    app = create_app(store)
    with app.app_context():
        c = app.test_client()
        yield c
    store.truncate()


def test_get_empty_items_view(client: FlaskClient):
    res = client.get('/items')
    assert res.status_code == 200
    data = json.loads(res.data.decode())
    assert data['items'] == []


def test_get_items_view(client: FlaskClient):
    store = get_test_store()
    store.put_item(Item(key='key', value='value'))

    res = client.get('/items')
    assert res.status_code == 200
    data = json.loads(res.data.decode())
    assert data['items'][0]['key'] == 'key'
    assert data['items'][0]['value'] == 'value'


def test_put_item_view(client: FlaskClient):
    res = client.put('/items/key', data='value')
    assert res.status_code == 201
    data = json.loads(res.data.decode())
    assert data['key'] == 'key'
    assert data['value'] == 'value'

    store = get_test_store()
    assert store.get_item('key').value == 'value'


def test_get_item_view(client: FlaskClient):
    store = get_test_store()
    store.put_item(Item(key='key', value='value'))

    res = client.get('/items/key')
    assert res.status_code == 200
    data = json.loads(res.data.decode())
    assert data['key'] == 'key'
    assert data['value'] == 'value'


def test_get_non_exists_item_view(client: FlaskClient):
    res = client.get('/items/non_exists')
    assert res.status_code == 404