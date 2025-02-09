from flask import current_app
from app.exceptions import InvalidDataError
from app.lib.helpers import to_json_dict
from celery.result import AsyncResult

def call(job_request):
    job_id = job_request.get('id')
    job_data = status(job_id)

    return { 'job': job_data }

def status(job_id):
    try:
        job = AsyncResult(job_id)

        return {
            'id': job_id,
            'status': job.state,
            'result': job.result
        }
    except ValueError as e:
        raise InvalidDataError(f"Invalid job id: {job_id}", data={ 'job': {'id': job_id }})
