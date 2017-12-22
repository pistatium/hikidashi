# coding: utf-8

from os import environ


SWAGGER_UI_HOST = environ.get('SWAGGER_UI_HOST')

BACKEND_NAME = 'dynamodb'
BACKEND_CONF = {
    'DYNAMODB_ENDPOINT_URL': environ.get('DYNAMODB_ENDPOINT_URL')
}
