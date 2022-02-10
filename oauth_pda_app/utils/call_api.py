import requests
from django.conf import settings


def get_api(request, url):
    """
    Envoie une requête au portail des assos en intégrant le token de
    connexion
    """
    return requests.get(
        "{}{}".format(settings.OAUTH_SETTINGS["api_base_url"], url),
        headers={
            'Authorization': 'Bearer {}'.format(request.session['token']['access_token']),
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    )
