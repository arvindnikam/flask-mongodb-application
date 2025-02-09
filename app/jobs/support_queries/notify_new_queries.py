import os
from flask import current_app
from celery import shared_task
# from app.services.support_queries import notify_new_queries as notify_new_queries_service

CELERY_MAX_RETRY = int(os.getenv('CELERY_MAX_RETRY', 3))
CELERY_RETRY_BACKOFF = int(os.getenv('CELERY_RETRY_BACKOFF', 30))

@shared_task(bind=True, max_retries=CELERY_MAX_RETRY)
def call(self, dummy_arg=None):
    current_app.logger.info(f"Started: notify_new_queries - dummy_arg: {dummy_arg}")
    try:
        # response = notify_new_queries_service.call()
        current_app.logger.info(f"Finished: create_execution - dummy_arg: {dummy_arg}")
        # return response
    except Exception as e:
        current_app.logger.error(f"Failed: create_execution - dummy_arg: {dummy_arg} with error: {e}")
        raise self.retry(exc=Exception(str(e)), countdown=CELERY_RETRY_BACKOFF * (2 ** self.request.retries))
