import os

port        =   os.getenv('FLOWER_PORT')
broker      =   os.getenv('CELERY_REDIS_URL')
broker_api  =   os.getenv('CELERY_REDIS_URL')
persistent  =   True
db          =   'flower'
auto_refresh=   False
purge_offline_workers   =   1 # sec
state_save_interval     =   1000 # ms
tasks_columns           =   "name,uuid,state,args,kwargs,result,received,started,runtime,worker,retries,exception,expires,eta"
