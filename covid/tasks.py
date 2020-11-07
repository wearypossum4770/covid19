from celery import shared_task
from .celery import app

# app = Celery('tasks', broker='pyamqp://guest@localhost//')


@shared_task
def add(x, y):
    return x + y
