# coding: utf-8

from typing import List

from .store import Store
from hikidashi.models.item import Item


class DynamoStore(Store):
    def get_items(self, **kwargs) -> List[Item]:
        pass

    def get_item(self, key: str) -> Item:
        pass

    def put_item(self, item: Item = None):
        pass
