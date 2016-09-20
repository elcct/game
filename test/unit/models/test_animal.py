import unittest
from datetime import datetime, timedelta

from models.animal import Animal
from models.animal_kinds import AnimalKinds

class TestAnimal(unittest.TestCase):
    def test_can_pet_and_feed(self):
        kind = 'cat'
        ak = AnimalKinds()

        animal = Animal(kind=kind, details=ak.get_json_definition(kind))

        happiness = animal.happiness
        animal.pet()
        self.assertGreater(animal.happiness, happiness)

        hunger = animal.hunger
        animal.feed()
        self.assertLess(animal.hunger, hunger)


    def test_can_update(self):
        kind = 'cat'
        ak = AnimalKinds()

        animal = Animal(kind=kind, details=ak.get_json_definition(kind))

        hour_ago = animal.created_at - timedelta(hours=1)
        animal.updated_at = hour_ago

        happiness = animal.happiness
        hunger = animal.hunger
        animal.update_stats()
        
        # animal should be more hungry and less happy
        self.assertLess(animal.happiness, happiness)
        self.assertGreater(animal.hunger, hunger)
