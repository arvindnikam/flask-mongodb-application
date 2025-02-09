from flask import request
from app.lib.helpers.response_helper import generate_response

def create():
    from app.services.support_queries import create as create_service

    request_json = request.json.get('query', {})
    response_data = create_service.call(request_json)
    generate_response(success=True, response_data={'status': 'success', 'message': "query submitted successfully", "data": response_data})

def update(query_id):
    from app.services.support_queries import update as update_service

    request_json = request.json.get('query', {})
    response_data = update_service.call(query_id, request_json)
    generate_response(success=True, response_data={'status': 'success', 'message': "query updated successfully", "data": response_data})

def search():
    from app.services.support_queries import search as search_service
    from app.lib.helpers.search_helper import get_search_options

    request_json = request.json
    conditions = request_json.get('conditions', {})
    search_options = get_search_options(request_json)

    response_data = search_service.call(conditions, **search_options)
    generate_response(success=True, response_data={'status': 'success', 'message': "queries found", "data": response_data})
