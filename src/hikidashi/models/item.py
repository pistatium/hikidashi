# coding: utf-8

from typing import NamedTuple


class Item(NamedTuple):
    key: str
    value: object
    created_at: int
    updated_at: int

    def to_dict(self):
        d = self._asdict()
        return d
