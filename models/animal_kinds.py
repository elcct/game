import json

class AnimalKinds:
    kinds = {
        "dog": {
            "happiness_decay": 1,
            "happiness_increase": 2,
            "hunger_decay": 10,
            "hunger_increase": 20,
        },
        "cat": {
            "happiness_decay": 2,
            "happiness_increase": 5,
            "hunger_decay": 10,
            "hunger_increase": 30,
        },
    }

    def get_kinds(self):
        return list(self.kinds.keys())

    def get_json_definition(self, kind):
        if kind in list(self.kinds.keys()):
            return json.dumps(self.kinds[kind])
        raise ValueError
