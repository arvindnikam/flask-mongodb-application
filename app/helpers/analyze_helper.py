def aggregation_pipeline(group_by, aggregates):
    pipeline = {'$group': {}}
    if isinstance(group_by, list):
        pipeline['$group']['_id'] = { field: f'${field}' for field in group_by }
    else:
        pipeline['$group']['_id'] = {f'{group_by}': f'${group_by}'}
        pipeline['$group']['count'] = { "$sum": 1 }
    if aggregates:
        for field_name, (operator, field_path) in aggregates.items():
            if operator == 'count':
                pipeline['$group'][field_name] = {'$sum': 1}
            else:
                pipeline['$group'][field_name] = { f'${operator}': f'${field_path}' }
    elif aggregates == {}:
        pipeline['$group']['count'] = { '$sum': 1 }
    return [pipeline]

# TODO: handle nested list in aggregation pipeline
# for field_name, (operator, field_path) in aggregates.items():
#     if '.' in field_path:  # Check for nested structures
#         split_path = field_path.split('.')
#         for sub_path in split_path:
#             if sub_path.endswith(']'):  # Identify array field
#                 pipeline.append({'$unwind': '$' + sub_path})
