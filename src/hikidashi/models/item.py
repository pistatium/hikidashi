# coding: utf-8

from typing import NamedTuple


class Item(NamedTuple):
    key: str
    value: object
    created_at: int
    updated_at: int
