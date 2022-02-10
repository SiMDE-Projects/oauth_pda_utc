from django.conf import settings
from oauthlib.oauth2 import WebApplicationClient
from rest_framework import serializers


class AuthorizationLink:
    """
    Classe dédiée à la génération du lien d'autorisation pour demander
    à l'utilisateur d'accepter le partage des données avec l'application
    """

    def __init__(self):
        # création du client oauth avec l'ID du client
        client = WebApplicationClient(settings.OAUTH_SETTINGS['client_id'])

        # construction de la requête d'autorisation oauth
        self.link = client.prepare_request_uri(
            settings.OAUTH_SETTINGS['authorization_url'],
            redirect_uri=settings.OAUTH_SETTINGS['redirect_uri'],
            scope=settings.OAUTH_SETTINGS['scopes'])


class AuthorizationLinkSerializer(serializers.Serializer):
    """
    Serializer pour AuthorizationLink
    """
    link = serializers.CharField()


class UserInfoSerializer(serializers.Serializer):
    """
    Serializer pour renvoyer au front les informations sur l'utilisateur
    connecté. Permet de filtrer la réponse du portail en récupérant les
    champs qui nous intéressent
    """
    id = serializers.UUIDField()
    email = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
