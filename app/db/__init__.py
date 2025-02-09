from redis import Redis

from bunnet import init_bunnet
from pymongo import MongoClient
import json

celery_redis = None

def init_db(app):
    init_celery_redis(app)
    init_application_db(app)

def init_celery_redis(app):
    global celery_redis
    celery_redis_url = app.config['CELERY_REDIS_URL']
    celery_redis = Redis.from_url(celery_redis_url)

def init_application_db(app):
    # Create Motor client
    application_db_uri = app.config['BASE_APPLICATION_DB_URI']
    mongo_client = MongoClient(application_db_uri, tz_aware=True)

    # Init bunnet with the Product document class
    application_database = mongo_client[app.config["BASE_APPLICATION_DB_NAME"]]
    init_bunnet(
        database=application_database,
        document_models=[
            "app.models.user.User",
            "app.models.location.Location",
            "app.models.support_query.SupportQuery",
        ]
    )
