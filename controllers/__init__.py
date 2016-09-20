from decorator import decorator
from connexion import NoContent, request

from models.user import User
from helpers.user import get_login_from_token

@decorator
def requires_auth(f: callable, *args, **kwargs):
    if 'Authentication' in request.headers:
        login = get_login_from_token(request.headers['Authentication'])
        user = User.query.filter(User.login==login).first()
        if not user:
            return NoContent, 401

        request.user = user
    return f(*args, **kwargs)
