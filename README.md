Virtual Pet Game
----------------

## Structure

`controllers` - API endpoints

`database` - DB initialization

`models` - definition of models

`helpers` - helpers functions, eg. jwt authentication

`swagger` - definition of the RESTful API

`test` - couple of unit tests

## API

API is defined in `swagger\swagger.yaml` file.
Example use of API can be found in `curl.txt` file.

### Paths:

/v1/user/login

/v1/user/register

/v1/animals

/v1/animal/kinds

/v1/animal/{id}/pet

/v1/animal/{id}/feed

/v1/animal/{id}/info

## Animals

Animal kinds are defined in `models/animal_kinds.py`. This could be later on
kept in the database.
Animal definition consists of `kind` name and properties like hunger increase,
happiness decrease that happens every hour.
When animal is pet or fed happiness increase or hunger decrease.

## Installation

Create new virtual environment using `virtualenv` and install requirements:

```
pip3 install -r requirements.txt
```

Create database:

```
python3 install.py
```

That should create `game.db` file in your project directory.

Start RESTful API:

```
python3 app.py
```

API should be available at 0.0.0.0:5000

## Tests

```
nosetests -vv --exe
```
