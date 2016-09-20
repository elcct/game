import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_can_set_and_compare_password(self):
        u = User()

        password = 'hello world'

        u.set_password(password)

        # password shouldn't be plain text
        self.assertNotEqual(u.password, password)

        result = u.compare_password(password)
        self.assertEqual(result, True)

        result = u.compare_password('no hello today')
        self.assertEqual(result, False)
