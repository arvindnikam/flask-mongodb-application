import requests
from flask import current_app
from app.exceptions import ClientError
from requests.exceptions import JSONDecodeError

def get(url, headers={}):
    headers['caller_id'] = 'markeplace_backend'
    current_app.logger.info(f"""Making GET call to {url}
    HEADERS: {headers}""")

    response = requests.get(f"{url}", headers=headers)
    validate_response_status(response)
    response_json = get_response_json(response)

    current_app.logger.info(f"""Finished GET call {url}
    RESPONSE: {response_json}""")

    return response_json

def post(url, data, headers={}):
    headers['caller_id'] = 'markeplace_backend'
    current_app.logger.info(f"""Making POST call to {url}
    HEADERS: {headers}
    REQUEST: {data}""")

    response = requests.post(f"{url}", json=data, headers=headers, timeout=10)
    validate_response_status(response)
    response_json = get_response_json(response)

    current_app.logger.info(f"""Finished POST call {url}
    RESPONSE: {response_json}""")

    return response_json

def validate_response_status(response):
    try:
        response_content = (response.content or b'').decode()
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        current_app.logger.error(f"""Http Error: {e}
        RESPONSE: {response_content}""")
        response_json = get_response_json(response)
        raise ClientError(response_json.get('message') or str(e), status_code = response.status_code)
    except requests.exceptions.ConnectionError as e:
        current_app.logger.error(f"""Error Connecting: {e}
        RESPONSE: {response_content}""")
        raise ClientError(response_json.get('message') or str(e), status_code = response.status_code)
    except requests.exceptions.ReadTimeout as e:
        current_app.logger.error(f"""Timeout Error: {e}
        RESPONSE: {response_content}""")
        raise ClientError(response_json.get('message') or str(e), status_code = response.status_code)
    except requests.exceptions.Timeout as e:
        current_app.logger.error(f"""Timeout Error: {e}
        RESPONSE: {response_content}""")
        raise ClientError(response_json.get('message') or str(e), status_code = response.status_code)
    except requests.exceptions.RequestException as e:
        current_app.logger.error(f"""OOps: Something Else {e}
        RESPONSE: {response_content}""")
        raise ClientError(response_json.get('message') or str(e), status_code = response.status_code)

def get_response_json(response):
    try:
        return response.json()
    except JSONDecodeError as e:
        return {}
