# coding: utf-8

from os import environ


SWAGGER_UI_HOST = environ.get('SWAGGER_UI_HOST')

BACKEND_NAME = 'dynamodb'
BACKEND_CONF = {
    'table_name': environ.get('DYNAMODB_TABLE_NAME'),
    'endpoint_url': environ.get('DYNAMODB_ENDPOINT_URL')
}
