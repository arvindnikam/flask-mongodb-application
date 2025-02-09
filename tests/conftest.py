import pytest
from app import create_app
from . import clear_db, seed_db

@pytest.fixture(autouse=True)
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    # Run around test suit
    clear_db()
    seed_db()
    yield app
    clear_db()

@pytest.fixture(autouse=True)
def client(app):
    return app.test_client()

@pytest.fixture(autouse=True)
def runner(app):
    return app.test_cli_runner()

# Run around every test without having to pass fixture explicitely to test method
@pytest.fixture(autouse=True)
def run_around_tests():
    yield
