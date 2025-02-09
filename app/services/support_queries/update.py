from app.exceptions import InvalidDataError
from app.repositories import _support_query_repository

def call(query_id, request):
    if not (support_query:=~_support_query_repository().get(query_id)):
        raise InvalidDataError('Invalid query id')

    _support_query_repository().update(support_query, request)
    return support_query
