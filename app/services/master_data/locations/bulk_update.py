from flask import current_app
from app.lib.helpers.search_helper import get_search_options, parse_conditions
from app.repositories import _location_repository

def call(request):
    conditions = request.get('conditions', {})
    update_params = request.get('update_params', {})

    search_conditions = parse_conditions(conditions)
    response = _location_repository().update_many(search_conditions, update_params)

    return {
        'matched_count': response.matched_count,
        'modified_count': response.modified_count
    }
