import unittest
from models.animal_kinds import AnimalKinds

class TestAnimalKinds(unittest.TestCase):
    def test_can_get_animal_kinds(self):
        ak = AnimalKinds()

        kinds = ak.get_kinds()
        self.assertGreater(len(kinds), 0)

        props = ['hunger_decay', 'hunger_increase', 'happiness_decay', 'happiness_increase']
        for kind in kinds:
            k = ak.get_json_definition(kind)

            for prop in props:
                self.assertEqual(prop in k, True)
