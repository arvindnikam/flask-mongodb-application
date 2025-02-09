from app.exceptions import InvalidDataError
from app.helpers.analyze_helper import aggregation_pipeline
from app.lib.helpers.search_helper import parse_conditions
from app.repositories import _location_repository

def call(conditions, group_by='status', aggregates={}):
    for key, agg_on in aggregates.items():
        if agg_on[0] not in ['count', 'sum', 'avg', 'min', 'max']:
            raise InvalidDataError(f'Invalid aggregate_function: {agg_on[0]}')

    search_conditions = parse_conditions(conditions)
    locations = ~_location_repository().find(search_conditions).aggregate(aggregation_pipeline(group_by, aggregates))

    aggs = [ { key: location_agg[key] for key in location_agg if key and key != '_id' } | location_agg['_id'] for location_agg in locations ]
    aggs = [ { key: value for key,value in agg.items() if key and key != 'None'} for agg in aggs ]

    # if isinstance(group_by, str):
    #     aggs = { agg[group_by]: agg['count'] for agg in aggs }

    return { 'aggs': aggs }
