# coding: utf-8

from hikidashi.backends.dynamo_store import DynamoStore
from hikidashi.settings import DYNAMODB_ENDPOINT_URL
from hikidashi.models.item import Item


def test_put_and_get():
    print(DYNAMODB_ENDPOINT_URL)
    store = DynamoStore(table_name='test_hikidashi', endpoint_url=DYNAMODB_ENDPOINT_URL)
    item = Item(key='test', value='test')
    store.put_item(item)

    assert store.get_item('test') == item
