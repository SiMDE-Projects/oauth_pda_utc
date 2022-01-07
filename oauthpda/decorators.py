from requests import Response


def is_sso_authenticated(func):
    def wrapper(request, *args, **kwargs):
        if 'token' not in request.session.keys():
            res = Response()
            res.status_code = 401
            res.reason = 'Unauthorized'
            return res

        token = request.session['token']
        request.headers['Authorization'] = 'Bearer {}'.format(token)

        return func(request, *args, **kwargs)

    return wrapper
