from celery import Celery
from celery.schedules import crontab
import feedparser

app = Celery('tasks', broker='redis://localhost//')

app.conf.update({
  'CELERYBEAT_SCHEDULE': {
    'echo': {
      'task': 'celery_task.echo',
      'schedule': crontab(minute='*/1')
    }
  }
})

@app.task(name='celery_task.echo')
def echo():
    rss = feedparser.parse("https://gigazine.net/news/rss_2.0/")
    for entry in rss.entries:
        print("記事のURL: " + entry.link)
        print("記事のタイトル: " + entry.title)
    return None
