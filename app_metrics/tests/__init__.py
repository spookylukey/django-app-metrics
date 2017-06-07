from celery import Celery
from django.conf import settings

# Ensure test config gets for Celery gets set up when running tests
app = Celery('app_metrics')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
