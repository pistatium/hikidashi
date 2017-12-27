# coding: utf-8

import pytest

from hikidashi.backends.store import Backends
from hikidashi.backends.dynamo_store import DynamoStore
from hikidashi.settings import BACKEND_NAME, BACKEND_CONF
from hikidashi.models.item import Item


@pytest.fixture()
def store():
    store = DynamoStore(table_name='test_hikidashi', endpoint_url=BACKEND_CONF['endpoint_url'])
    yield store
    store.truncate()


@pytest.mark.skipif(BACKEND_NAME != Backends.DYNAMODB.value, reason='Backend is not dynamodb')
def test_put_and_get_string(store):
    item = Item(key='test', value='test')
    store.put_item(item)

    assert store.get_item('test').value == item.value


@pytest.mark.skipif(BACKEND_NAME != Backends.DYNAMODB.value, reason='Backend is not dynamodb')
def test_put_and_get_integer(store):
    store = DynamoStore(table_name='test_hikidashi', endpoint_url=BACKEND_CONF['endpoint_url'])
    item = Item(key='test', value=123456789)
    store.put_item(item)

    assert store.get_item('test').value == item.value


@pytest.mark.skipif(BACKEND_NAME != Backends.DYNAMODB.value, reason='Backend is not dynamodb')
def test_put_and_get_float(store):
    store = DynamoStore(table_name='test_hikidashi', endpoint_url=BACKEND_CONF['endpoint_url'])
    item = Item(key='test', value=0.1)
    store.put_item(item)

    assert store.get_item('test').value == item.value