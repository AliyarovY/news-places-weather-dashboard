from celery import Celery
from celery.schedules import crontab
from django.core.mail import send_mail
from django.conf import settings
from constance import config
from django.utils.timezone import now

from .models import News

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task
def today_news_send():
    today = now().date()
    today_news_titles = News.objects.filter(pub_date__date=today).values_list('title', flat=True)

    for title in today_news_titles:
        send_mail(
            config.SUBJECT,
            f'{title}: \n{config.MESSAGE}',
            settings.EMAIL_HOST_USER,
            config.RECIPIENTS,
            fail_silently=False,
        )


app.conf.beat_schedule = {
    'my-task': {
        'task': 'news.tasks.today_news_send',
        'schedule': crontab(**config.TIME),
    },
}
