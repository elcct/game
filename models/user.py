from database.base import Base

from sqlalchemy import Column, Integer, String
import hashlib, uuid

# User defines our user model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String(32))
    password = Column(String(128))
    password_salt = Column(String(32))

    def __init__(self, id=None, login=None):
        self.id = id
        self.login = login

    # get_password_hash creates salted password hash using sha512
    def get_password_hash(self, password):
        return hashlib.sha512(password.encode('utf-8') + self.password_salt.encode('utf-8')).hexdigest()

    # set_password stores salt and hash out of given password
    def set_password(self, password):
        # TODO: storage of this data can be optimized later
        self.password_salt = uuid.uuid4().hex
        self.password = self.get_password_hash(password)

    # compare_password computes hash of given password and compares with the
    # stored password hash
    def compare_password(self, password):
        h = self.get_password_hash(password)
        return self.password == h
