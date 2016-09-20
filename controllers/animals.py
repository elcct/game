from decorator import decorator
from connexion import NoContent, request

from database.base import db_session
from controllers import requires_auth
from models.animal import Animal
from models.animal_kinds import AnimalKinds

@requires_auth
def list():

    animals = Animal.query.filter(Animal.user_id==request.user.id)
    res = [animal.to_dict() for animal in animals]

    return res, 200

def kinds():
    return AnimalKinds().get_kinds(), 200

@requires_auth
def animal(kind=None):
    if not kind or 'kind' not in kind:
        return NoContent, 400

    ak = AnimalKinds()
    kinds = ak.get_kinds()

    kind = kind['kind']
    if kind not in kinds:
        return NoContent, 404

    animal = Animal(user_id=request.user.id, kind=kind, details=ak.get_json_definition(kind))
    db_session.add(animal)
    db_session.commit()

    return animal.to_dict(), 200

@requires_auth
def pet(id=None):
    if not id:
        return NoContent, 400

    animal = Animal.query.filter(Animal.id==id,Animal.user_id==request.user.id).first()
    if not animal:
        return NoContent, 404

    animal.update_stats()
    animal.pet()
    db_session.commit()

    return animal.to_dict(), 200


@requires_auth
def feed(id=None):
    if not id:
        return NoContent, 400

    animal = Animal.query.filter(Animal.id==id,Animal.user_id==request.user.id).first()
    if not animal:
        return NoContent, 404

    animal.update_stats()
    animal.feed()
    db_session.commit()

    return animal.to_dict(), 200

@requires_auth
def info(id=None):
    if not id:
        return NoContent, 400

    animal = Animal.query.filter(Animal.id==id,Animal.user_id==request.user.id).first()
    if not animal:
        return NoContent, 404

    animal.update_stats()
    animal.info()

    return animal.to_dict(), 200
