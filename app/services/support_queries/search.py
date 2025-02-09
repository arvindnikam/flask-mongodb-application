from app.repositories import _support_query_repository
from app.lib.helpers.search_helper import parse_conditions

def call(conditions, offset=None, limit=None, sort_column=None, sort_order=None):
    _sort = f"-{sort_column}" if sort_column and sort_order=='desc' else sort_column

    search_conditions = parse_conditions(conditions)
    support_queries_query = _support_query_repository().find(search_conditions)
    support_queries = ~support_queries_query.skip(offset).limit(limit).sort(_sort)

    return {
        "support_queries": support_queries,
        "offset": offset,
        "limit": limit,
        "sort_column": sort_column,
        "sort_order": sort_order,
        "count": len(support_queries),
        "total": support_queries_query.count()
    }
