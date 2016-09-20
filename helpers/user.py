import jwt
import os
import base64

secret = os.getenv('GAME_SECRET', 'secret')

def get_token_from_login(login):
    token = jwt.encode({'login': login}, secret, algorithm='HS256')
    return token.decode('ascii')

def get_login_from_token(token):
    token = token.replace('Bearer ', '')
    payload = jwt.decode(bytes(token.encode('ascii', 'ignore')), secret, algorithms=['HS256'])
    return payload.get('login', None)
