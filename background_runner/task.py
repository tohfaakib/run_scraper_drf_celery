from celery import shared_task
import time
from imdb.script import main

@shared_task
def sleepy(duration):
    time.sleep(duration)
    return "awake now."


@shared_task
def start_tracking(start_url, start_page_number):
    main(start_url, start_page_number)

