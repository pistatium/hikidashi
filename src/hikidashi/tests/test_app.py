# coding: utf-8

import json
import pytest
import copy

from hikidashi.app import create_app
from hikidashi.settings import BACKEND_NAME, BACKEND_CONF


@pytest.fixture
def client(request):
    conf = copy.deepcopy(BACKEND_NAME)
    conf['TABLE_NAME'] = 'test_hikidashi'
    c = create_app(BACKEND_NAME, **conf).test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return c