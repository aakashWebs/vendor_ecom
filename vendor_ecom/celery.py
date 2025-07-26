import os
import time
from celery import Celery
from kombu.exceptions import OperationalError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendor_ecom.settings')

app = Celery('vendor_ecom')

# Load config from settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Retry logic to wait for Redis broker to be ready
max_retries = 5
retry_delay = 5  # seconds

for i in range(max_retries):
    try:
        # Try to get default channel to test connection
        _ = app.connection().default_channel
        break
    except OperationalError:
        if i < max_retries - 1:
            print(f"Redis broker not ready, retrying in {retry_delay} seconds...")
            time.sleep(retry_delay)
        else:
            print("Could not connect to Redis broker after retries.")
            raise

# Auto-discover all `tasks.py` from every app
app.autodiscover_tasks()
