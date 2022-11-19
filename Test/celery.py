from celery import Celery
import os
# from blog.models import Blog

# from django.contrib.auth.models import User

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Test.settings")

app = Celery('first' , broker = 'amqp://localhost')
app.autodiscover_tasks()

@app.task
def send_blog():
   user_ids = User.objects.values_list('id' , flat=True)
   Blog.objects.bulk_create(
      Blog(
         user = uid,
         title = 'blog1',
         text = 'This is blog1',
      )
      for uid in user_ids)
