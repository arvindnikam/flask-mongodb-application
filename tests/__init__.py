## Documents 
#  https://pytest-flask.readthedocs.io/en/latest/tutorial.html
#  https://pytest-factoryboy.readthedocs.io/en/stable/
#  https://testdriven.io/blog/flask-pytest/
#  [Pending] https://docs.celeryq.dev/en/4.4.0/userguide/testing.html

## How to run tests
#  FLASK_ENV=test python -m pytest

## Run tests in specific folder
#  FLASK_ENV=test python -m pytest tests/unit

## Run tests in specific file
#  FLASK_ENV=test python -m pytest tests/unit/app/controllers/base_controller_test.py

## Run specific test function
#  FLASK_ENV=test python -m pytest tests/unit/app/controllers/base_controller_test.py::test_index

## Run tests matching pattern
#  FLASK_ENV=test python -m pytest tests/unit/app/controllers/base_controller_test.py -k "index"

## Run tests to generate code coverage report
#  FLASK_ENV=test coverage run -m pytest
#  coverage html
#  open htmlcov/index.html

from app.repositories import (
    _location_repository,
    _support_query_repository
)

def clear_db():
    _location_repository().find().delete().run()
    _support_query_repository().find().delete().run()

def seed_db():
    pass
