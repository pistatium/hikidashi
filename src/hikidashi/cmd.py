# coding: utf-8

import sys
from os.path import dirname
from logging import getLogger, StreamHandler, DEBUG

import click

from .app import create_app

from hikidashi.settings import BACKEND_NAME, BACKEND_CONF
from hikidashi.backends.store import Backends

handler = StreamHandler(sys.stdout)
logger = getLogger(dirname(__name__))
logger.propagate = False
logger.addHandler(handler)


@click.group()
def cmd():
    pass


@cmd.command()
@click.option('--debug', is_flag=True, default=True)
@click.option('--port', type=int, default='8000')
@click.option('--host', default='0.0.0.0')
def runserver(host, port, debug):
    store = Backends.get_store(BACKEND_NAME, **BACKEND_CONF)
    app = create_app(store)
    if debug:
        app.debug = True
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)
    app.run(host=host, port=port)


def main():
    cmd()


if __name__ == '__main__':
    main()
