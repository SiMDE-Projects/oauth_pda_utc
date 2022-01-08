import requests
from django.conf import settings


def _call_api(url: str, method: str = "GET", parameters: dict = None, body: dict = None):
    return requests.request(method, settings.OAUTH_SETTINGS.get('api_base_url', '') + url, params=parameters, json=body)


def call_get_api(url: str, parameters: dict = None):
    return _call_api(url, parameters=parameters)


def call_post_api(url: str, body: dict = None):
    return _call_api(url, "POST", body=body, parameters=None)


def call_patch_api(url, body: dict = None, parameters: dict = None):
    return _call_api(url, "PATCH", body=body, parameters=parameters)


def call_put_api(url, body: dict = None, parameters: dict = None):
    return _call_api(url, "PUT", body=body, parameters=parameters)


def call_delete_api(url, body: dict = None, parameters: dict = None):
    return _call_api(url, "DELETE", body=body, parameters=parameters)