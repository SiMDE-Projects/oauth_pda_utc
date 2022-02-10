from django.contrib.auth.backends import RemoteUserBackend


class OAuthBackend(RemoteUserBackend):
    def authenticate(self, request, remote_user):
        user = super(OAuthBackend, self).authenticate(request, remote_user["id"])
        user.first_name = remote_user["firstname"]
        user.last_name = remote_user["lastname"]
        user.email = remote_user["email"]
        user.backend = "oauth_pda_app.backend.OAuthBackend"
        user.save()
        return user
