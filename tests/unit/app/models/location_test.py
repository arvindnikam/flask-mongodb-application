import pytest
from bson import ObjectId
from bunnet import PydanticObjectId
from app.exceptions import InvalidDataError
from app.models import BaseDocument
from app.models.location import Location
from app.repositories import _location_repository
from tests.factories import location_factory

@pytest.fixture
def run_around():
    _location_repository().find().delete().run()
    yield
    _location_repository().find().delete().run()
    
def test_workforce_model_with_factory(location_factory):
    location = location_factory()
    assert location.city is not None
    assert location.area is not None
    assert location.pincode is not None
   
def test_location_model_with_cleanup(location_factory):
    def validate_location_count(count):
        location = _location_repository().find()
        assert location.count() == count

    validate_location_count(0)
    location = location_factory()
    assert location.id is not None
    validate_location_count(1)
    
def test_location_model_settings():
    assert issubclass(Location, BaseDocument)

    assert hasattr(Location, 'Settings')

    assert hasattr(Location.Settings, 'name')
    assert Location.Settings.name == "locations"
    
    assert hasattr(Location.Settings, 'validate_on_save')
    assert Location.Settings.validate_on_save == True

    assert hasattr(Location.Settings, 'use_state_management')
    assert Location.Settings.use_state_management == True
