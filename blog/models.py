from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):
    writer = models.ForeignKey(User , on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    body = models.TextField()

    date_created = models.DateTimeField(auto_now = True)
    date_modified = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.title}'