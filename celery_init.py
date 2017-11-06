from __future__ import absolute_import
from celery import Celery
from kombu import Exchange, Queue
redis_host = 'redis://production-cache.haoefi.0001.usw1.cache.amazonaws.com:6379'
#redis_host = 'redis://ip-172-31-15-245.us-west-1.compute.internal:6379'

celery_app = Celery('indexer', broker=redis_host,
                    backend=redis_host,
                    include=['tasks'])
celery_app.config_from_object('celeryconfig')
celery_app.conf.update(CELERY_DEFAULT_QUEUE='analytics_worker')
celery_app.conf.update(CELERY_QUEUES=(Queue('analytics_worker', Exchange('analytics_worker'),
                                            routing_key='analytics_worker'),))

# celery_app.autodiscover_tasks(packages = ['index', 'search'],related_name='tasks', force=True)
if __name__ == '__main__':
    celery_app.start()
