import json
import datetime
from sqlalchemy import Column, Integer, String, UnicodeText, DateTime

from database.base import Base

# Animal defines our animal model
class Animal(Base):
    DEFAULT_HAPPINESS = 100000
    DEFAULT_HUNGER = 0
    TOO_HUNGRY_TO_LIVE = 100000

    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)

    name = Column(String(32))
    kind = Column(String(32))

    # happiness if goes below 0 animal dies
    happiness = Column(Integer)
    # hunger if goes below 0 animal dies
    hunger = Column(Integer)

    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    # keeps JSON data about animal attributes
    details = Column(UnicodeText())

    def __init__(self, id=None, user_id=None, name=None, kind=None, details=None):
        self.id = id
        self.user_id = user_id
        self.name = name
        self.kind = kind
        self.details = details
        self.hunger = self.DEFAULT_HUNGER
        self.happiness = self.DEFAULT_HAPPINESS
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = datetime.datetime.utcnow()

    # update updates animal happiness and hunger according to details
    def update_stats(self):
        details = json.loads(self.details)

        hours_since = int(((datetime.datetime.utcnow() - self.updated_at)).total_seconds() / 3600)

        if hours_since > 0:
            self.happiness = self.happiness - details['happiness_decay'] * hours_since
            self.hunger = self.hunger + details['hunger_increase'] * hours_since
            self.updated_at = datetime.datetime.utcnow()

    def feed(self):
        details = json.loads(self.details)

        self.hunger = self.hunger - details['hunger_decay']
        self.updated_at = datetime.datetime.utcnow()

    def pet(self):
        details = json.loads(self.details)

        self.happiness = self.happiness + details['happiness_increase']
        self.updated_at = datetime.datetime.utcnow()

    def is_dead(self):
        return self.happiness < 0 or self.hunger > self.TOO_HUNGRY_TO_LIVE

    def to_dict(self):
        return {
            'id': self.id,
            'kind': self.kind,
            'happiness': self.happiness,
            'hunger': self.hunger,
        }
