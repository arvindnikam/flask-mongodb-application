import json, re
from bson import ObjectId
import pytz
from dateutil.parser import parse as datetime_parser
from dateutil.relativedelta import relativedelta
from datetime import date, datetime, time, timezone
from app.lib.helpers.extensions import MongoEncoder

# Common Operations

"""Generate a random string of fixed length """
def random_string(stringLength=10):
    import random, string
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))

def parse_json(json_str): return json.loads(json_str)

def to_json(obj):
    obj = stringify_keys(obj)
    return json.dumps(obj, cls=MongoEncoder)

def to_json_dict(obj): return json.loads(to_json(obj))

def stringify_keys(obj):
    """Recursively replaces keys of specified non-string types with their string representations."""
    if isinstance(obj, dict):
        for key, value in list(obj.items()):
            if isinstance(key, (ObjectId, datetime, date, time, Exception)):
                obj.pop(key)
                key = str(key)
            obj[key] = stringify_keys(value)

    elif isinstance(obj, list):
        return [stringify_keys(item) for item in obj]

    return obj

# Datetime arithmatic
def current_time(): return datetime.now().astimezone()

def today(): return date.today()

def parse_datetime(obj): return obj if isinstance(obj, datetime) else datetime_parser(obj)

def datetime_ago(**delta): return current_time()-relativedelta(**delta)

def datetime_from_now(**delta): return current_time()+relativedelta(**delta)

def date_ago(**delta): return today()-relativedelta(**delta)

def date_from_now(**delta): return today()+relativedelta(**delta)

# Datetime timezone change
def tz_utc(dt): return dt.astimezone(tz=timezone.utc)

def tz_ist(dt): return dt.astimezone(pytz.timezone('Asia/Kolkata'))

def tz_local(dt): return dt.astimezone(tz=None)

def flatten(lst): return [element for item in lst for element in flatten(item)] if type(lst) is list else [lst]

def to_lower(match_obj):
    if match_obj.group() is not None:
        return match_obj.group().lower()
    return ''

def underscore(word):
    word = re.sub(r'[A-Z]', lambda x: f"_{to_lower(x)}", word)
    return re.sub("(^_*|_*$)", '', word)

def pluralize(word):
    word = underscore(word)
    if re.search('[sxz]$', word) or re.search('[^aeioudgkprt]h$', word):
        return re.sub('$', 'es', word)

    elif re.search('[aeiou]y$', word):
        return re.sub('y$', 'ies', word)

    else:
        return word + 's'

def dig(obj, keys=[]):
    if type(obj)==dict:
        if len(keys) == 0: return None
        if len(keys) == 1: return obj.get(keys[0])
        return dig(obj.get(keys[0]), keys[1:])
    else:
        return None

def flatten_dict(d, parent_key='', sep='.'):
    flattened_dict = {}
    for k, v in dict(d).items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            flattened_dict.update(flatten_dict(v, new_key, sep=sep))
        else:
            flattened_dict[new_key] = v
    return flattened_dict
