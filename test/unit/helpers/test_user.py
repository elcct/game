import unittest
from helpers.user import *

class TestUser(unittest.TestCase):
    def test_can_encode_and_decode_jwt_token(self):
        login = 'hello!'
        token = get_token_from_login(login)
        result = get_login_from_token(token)
        self.assertEqual(result, login)
        
