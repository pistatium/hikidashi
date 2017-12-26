# coding: utf-8

import json
import pytest
import copy

from hikidashi.app import create_app
from hikidashi.backends.store import Backends
from hikidashi.settings import BACKEND_NAME, BACKEND_CONF


@pytest.fixture
def client(request):
    conf = copy.deepcopy(BACKEND_CONF)
    conf['table_name'] = 'test_hikidashi'
    store = Backends.get_store(BACKEND_NAME, **conf)
    c = create_app(store).test_client()

    def teardown():
        store.truncate()

    request.addfinalizer(teardown)
    return c


def test_get_view(client):
    pass