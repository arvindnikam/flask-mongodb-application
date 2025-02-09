from bunnet import Document
from flask import current_app
from app.exceptions import InvalidDataError
from app.repositories import _location_repository

def call(location, request):
    if not isinstance(location, Document): 
        location = ~_location_repository().get(location)

    if not location:
        raise InvalidDataError('Invalid location')

    _location_repository().update(location, request)
    current_app.logger.info("Finished: location update")

    return location
