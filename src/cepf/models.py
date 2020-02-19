from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Officer(AbstractUser):

    class Meta:
        db_table = 'Officer'
        verbose_name_plural = 'Officer'

    def names():
        return self.first_name + ' ' + self.last_name

class Community(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    communication_channel = models.CharField(max_length=50)
    engagement_period = models.CharField(max_length=5)
    engagement_period_multipler = models.IntegerField()

    class Meta:
        db_table = 'Community'
        verbose_name_plural = 'Community'

class Appointment(models.Model):
    date = models.DateTimeField()
    officers = models.ManyToManyField(Officer)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    class Meta:
        db_table= 'Appointment'
        verbose_name_plural = 'Appointment'

class Post(models.Model):
    post = models.CharField(max_length=250)
    user = models.ForeignKey(Officer, on_delete=models.CASCADE)
