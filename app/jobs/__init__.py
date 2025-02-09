from uuid import uuid4
from app.lib.helpers.flask_helper import current_request_id, current_caller_id

def generate_task_id():
    request_id = current_request_id() or ''
    caller_id = current_caller_id() or ''
    task_id = str(uuid4())

    return '::'.join((request_id, caller_id, task_id))

def schedule(job, *args, **kwargs):
    job.apply_async(args, kwargs, task_id=generate_task_id())
