from django.http import HttpResponse


def require_sso_authenticated(func):
    def wrapper(self, request, *args, **kwargs):
        print(request.session)
        if not request.session or 'token' not in request.session.keys():
            return HttpResponse('Unauthorized', status=401)

        token = request.session['token']
        request.META['HTTP_AUTHORIZATION'] = 'Bearer {}'.format(token)

        return func(self, request, *args, **kwargs)

    return wrapper
