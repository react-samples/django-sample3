import os
import django
from celery import Celery
from celery.schedules import crontab
import feedparser

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoApp.settings')

app = Celery('djangoApp')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update({
  'CELERYBEAT_SCHEDULE': {
    'echo': {
      'task': 'celery_task.fetch',
      'schedule': crontab(minute='*/1')
    }
  }
})

django.setup()

from .models import Page

@app.task(name='celery_task.fetch')
def fetch():
    rss = feedparser.parse("https://gigazine.net/news/rss_2.0/")
    for entry in rss.entries:
        try:
            page_exists = Page.objects.get(href=entry.link)
        except Page.DoesNotExist:
            page = Page.objects.create(
                title=entry.title,
                href=entry.link
            )
            page.save()
