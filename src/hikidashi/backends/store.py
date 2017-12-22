# coding: utf-8

from typing import List
from enum import Enum
from abc import ABCMeta, abstractmethod

from hikidashi.models.item import Item


class Backends(Enum):
    DYNAMODB = 'dynamodb'

    @classmethod
    def get_store(cls, backend: str, **kwargs) -> 'Store':
        if backend == cls.DYNAMODB.value:
            from .dynamo_store import DynamoStore
            return DynamoStore(**kwargs)
        raise NotImplemented


class Store(metaclass=ABCMeta):

    @abstractmethod
    def get_items(self, **kwargs) -> List[Item]:
        ...

    @abstractmethod
    def get_item(self, key: str) -> Item:
        ...

    @abstractmethod
    def put_item(self, item: Item=None):
        ...
