import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hbrparse.settings')

app = Celery('hbrparse')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

argv = [
        'worker',
        '-l=DEBUG',
        '-P=eventlet',
        '--without-gossip',
        '--without-mingle',
        '--without-heartbeat',
        '-Ofair',
    ]

if __name__ == '__main__':
    app.worker_main(argv)