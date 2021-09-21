from celery import Celery
from time import sleep


CELERY_BROKER_URL = "amqp://admin:admin@rabbitmq:5672/"
CELERY_RESULT_BACKEND = "mongodb://db:27017/testcel"


celery = Celery(__name__, broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task()
def add_nums(a, b):
   sleep(10)
   return a + b
