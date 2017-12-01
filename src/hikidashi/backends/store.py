# coding: utf-8

from typing import List
from abc import ABCMeta, abstractmethod

from hikidashi.models.item import Item


class Store(metaclass=ABCMeta):

    @abstractmethod
    def get_items(self, **kwargs) -> List[Item]:
        ...

    @abstractmethod
    def get_item(self, key: str) -> Item:
        ...

    @abstractmethod
    def put_item(self, key: str=None, value: str=None, item: Item=None):
        ...
