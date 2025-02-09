from app.exceptions import InvalidDataError

def validate_presence(request, keys):
    if type(keys)!=list: keys = [keys]
    for key in keys:
        if not request.get(key):
            raise InvalidDataError(f"{key} cannot be blank")

def asset(asset_type, asset_name):
    from flask import current_app
    import os, textwrap
    return os.path.join(current_app.root_path, f"assets/{asset_type}", asset_name)

def try_exec(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        return e
