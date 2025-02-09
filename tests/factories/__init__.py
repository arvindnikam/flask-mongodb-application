import factory
from faker import Factory as FakerFactory
from pytest_factoryboy import register
from app.lib.helpers import random_string
from app.models.location import Location
from app.models.support_query import SupportQuery

faker = FakerFactory.create()

@register
class LocationFactory(factory.Factory):
    city = factory.Faker('city')
    area = factory.Faker('word')
    pincode = factory.Faker('postcode')

    @classmethod
    def _after_postgeneration(cls, obj, create, results=None):
        if create:  # Ensure this is executed only when creating an object
            obj.insert()

    class Meta:
        model = Location


@register
class SupportQueryFactory(factory.Factory):
    # user = factory.SubFactory(UserFactory)
    # user_id = factory.SelfAttribute('user.id')
    assistence_required = random_string()
    description = factory.Faker('text')
    status = 'created'
    user_type = 'user'

    @classmethod
    def _after_postgeneration(cls, obj, create, results=None):
        if create:  # Ensure this is executed only when creating an object
            obj.insert()

    class Meta:
        model = SupportQuery
