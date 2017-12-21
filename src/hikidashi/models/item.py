# coding: utf-8

from typing import NamedTuple
from time import time


class Item(NamedTuple):
    key: str
    value: str
    created_at: int = time()
    updated_at: int = time()

    def to_dict(self):
        d = self._asdict()
        d['updated_at'] = time()
        return d
