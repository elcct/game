from connexion import NoContent

from models.user import User
from helpers.user import get_token_from_login
from database.base import db_session

def login(user=None):
    if not user['login'] or not user['password']:
        return NoContent, 400

    login = user['login']
    password = user['password']

    user = User.query.filter(User.login==login).first()
    if not user:
        return NoContent, 404

    if not user.compare_password(password):
        return NoContent, 401

    return {
        'token': get_token_from_login(login)
    }

def register(user=None):
    if not user['login'] or not user['password']:
        return NoContent, 400

    login = user['login']
    password = user['password']

    user = User.query.filter(User.login==login).first()
    if user:
        return NoContent, 409

    user = User(login=login)
    user.set_password(password)

    db_session.add(user)
    db_session.commit()

    return NoContent, 200
