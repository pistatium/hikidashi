# coding: utf-8

import sys
from os.path import dirname
from logging import getLogger, StreamHandler

from .app import create_app
from .settings import BACKEND_CONF, BACKEND_NAME
from .backends.store import Backends


handler = StreamHandler(sys.stdout)
logger = getLogger(dirname(__name__))
logger.propagate = True
logger.addHandler(handler)

store = Backends.get_store(BACKEND_NAME, **BACKEND_CONF)
app = create_app(store)
