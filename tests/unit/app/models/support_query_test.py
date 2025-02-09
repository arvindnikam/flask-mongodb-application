import pytest
from bson import ObjectId
from bunnet import PydanticObjectId
from app.exceptions import InvalidDataError
from app.models import BaseDocument
from app.models.support_query import SupportQuery
from app.repositories import _support_query_repository
from tests.factories import support_query_factory

@pytest.fixture
def run_around():
    _support_query_repository().find().delete().run()
    yield
    _support_query_repository().find().delete().run()
    
def test_workforce_model_with_factory(support_query_factory):
    support_query = support_query_factory()
    # assert support_query.user_id is not None
    # assert support_query.user_id == user.id
    assert support_query.assistence_required is not None
    assert support_query.status is not None
    assert support_query.user_type is not None
   
def test_support_query_model_with_cleanup(support_query_factory):
    def validate_support_query_count(count):
        support_query = _support_query_repository().find()
        assert support_query.count() == count

    validate_support_query_count(0)
    support_query = support_query_factory()
    assert support_query.id is not None
    validate_support_query_count(1)

def test_support_query_model_settings():
    assert issubclass(SupportQuery, BaseDocument)

    assert hasattr(SupportQuery, 'Settings')

    assert hasattr(SupportQuery.Settings, 'name')
    assert SupportQuery.Settings.name == "support_queries"
