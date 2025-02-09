# https://github.com/Workable/flask-log-request-id

import os, yaml
from logging.config import dictConfig
from flask_log_request_id import RequestID
from dotenv import load_dotenv
from celery import Celery, Task
from celery.schedules import crontab
from app.lib.helpers.logging_helper import RequestIDLogFilter, CallerIDLogFilter

class BaseConfig(object):
    load_dotenv(dotenv_path=f'.env')
    ENV = os.getenv('FLASK_ENV')
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')

    BASE_APPLICATION_DB_URI = os.getenv('BASE_APPLICATION_DB_URI')
    BASE_APPLICATION_DB_NAME = os.getenv('BASE_APPLICATION_DB_NAME')

    CELERY_REDIS_URL = os.getenv('CELERY_REDIS_URL')
    CELERY = dict(
        # task_always_eager = True,
        broker_url=CELERY_REDIS_URL,
        result_backend=CELERY_REDIS_URL,
        task_ignore_result=False,
        task_default_queue='default',
        task_serializer = 'dill',
        result_serializer = 'dill',
        accept_content = ['dill', 'application/json', 'application/x-python-serialize']
    )
    CELERY_MAX_RETRY = int(os.getenv('CELERY_MAX_RETRY', 3))
    CELERY_RETRY_BACKOFF = int(os.getenv('CELERY_RETRY_BACKOFF', 30))

    END_POINTS = {
        'communication-api': {
            'email': 'https://communication-api/api/v1/communications/send_email'
        },
    }


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    CELERY_SCHEDULE_NOTIFY_NEW_QUERIES = crontab(minute='*/10')

config = {
    "development": "app.config.DevelopmentConfig",
}

def configure_app(app):
    config_name = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[config_name]) # object-based default configuration
    configure_logger(app)

# To use within application
# app.config[key]

def configure_celery(app) -> Celery:
    import dill
    from kombu.serialization import pickle_loads, pickle_protocol, registry
    from kombu.utils.encoding import str_to_bytes

    def register_dill():
        def encode(obj, dumper=dill.dumps):
            return dumper(obj, protocol=pickle_protocol)

        def decode(s):
            return pickle_loads(str_to_bytes(s), load=dill.load)

        registry.register(
            name='dill',
            encoder=encode,
            decoder=decode,
            content_type='application/x-python-serialize',
            content_encoding='binary'
        )

    register_dill()

    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def configure_logger(app):
    dictConfig(yaml.full_load(open(f'config/{os.getenv("FLASK_ENV")}/logging.conf')))
    RequestID(app)
    app.logger.addFilter(RequestIDLogFilter())
    app.logger.addFilter(CallerIDLogFilter())
