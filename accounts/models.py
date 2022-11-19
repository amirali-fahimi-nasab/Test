from django.db import models

from datetime import timedelta , datetime , timezone
# Create your models here.



class Profile(models.Model):
    first_name = models.CharField(max_length= 200)
    last_name = models.CharField(max_length = 200)
    email = models.EmailField()
    mobile = models.CharField(max_length=16)

    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.date_created.strftime('%d-%m-%Y')}"




class VerifyEmail(models.Model):
     new_email= models.CharField(max_length = 32)
     old_email = models.CharField(max_length = 32)




class VerifyMobile(models.Model):

    def is_expired(self):
        return timezone.now() - self.date_created > timedelta(2)
    email = models.EmailField()
    mobile = models.CharField(max_length = 20)
    verify = models.BooleanField(default = True)

    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.mobile} , {self.email}'