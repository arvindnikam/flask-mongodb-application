from app.repositories import _support_query_repository

def call(request):
    support_query = _support_query_repository().create(**request)
    return support_query
