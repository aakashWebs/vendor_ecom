# vendor/tasks.py
from celery import shared_task
import requests
import redis
import json

r = redis.Redis(host='redis_broker', port=6379, db=1)

@shared_task
def fetch_data_from_api(url):
    response = requests.get(url)
    data = response.json()
    # r.set('api_response', json.dumps(data))
    return data
