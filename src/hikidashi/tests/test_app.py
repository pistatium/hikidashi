# coding: utf-8

import json
import pytest
import copy

from flask.testing import FlaskClient

from hikidashi.app import create_app
from hikidashi.backends.store import Backends
from hikidashi.settings import BACKEND_NAME, BACKEND_CONF


@pytest.fixture
def client(request):
    conf = copy.deepcopy(BACKEND_CONF)
    conf['table_name'] = 'test_hikidashi'
    store = Backends.get_store(BACKEND_NAME, **conf)
    app = create_app(store)
    with app.app_context():
        c = app.test_client()
        yield c
    store.truncate()


def test_get_Item_view(client: FlaskClient):
    res = client.get('/items')
    assert res.ok
