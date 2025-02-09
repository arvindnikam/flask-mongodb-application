from flask import request
from app.lib.helpers.response_helper import generate_response
from app.lib.helpers.search_helper import get_search_options

def search():
    from app.services.master_data.locations import search as search_service

    request_json = request.json
    conditions = request_json.get('conditions', {})
    search_options = get_search_options(request_json)

    response_data = search_service.call(conditions, **search_options)
    generate_response(success=True, response_data={'status': 'success', 'message': "locations found", "data": response_data})

def analyze():
    from app.services.master_data.locations import analyze as analyze_service

    conditions = request.json.get('conditions', {})
    group_by = request.json.get('group_by', 'city')
    aggregate_function = request.json.get('aggregate_function', 'count')
    aggregate_on = request.json.get('aggregate_on')
    response_data = analyze_service.call(conditions, group_by, aggregate_function, aggregate_on)
    generate_response(success=True, response_data={'status': 'success', 'message': "locations found", "data": response_data})
