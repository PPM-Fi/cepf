from django.db import models
from django.contrib.auth.models import AbstractUser

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

class Feedback(models.Model):
    attendance = models.IntegerField()
    reception = models.IntegerField()
    impact = models.IntegerField()
    notes = models.TextField()

    class Meta:
        db_table = 'Feedback'
        verbose_name_plural = 'Feedback'

class Appointment(models.Model):
    date = models.DateTimeField()
    feedback = models.OneToOneField(Feedback, null=True, blank=True, on_delete=models.SET_NULL)
    officers = models.ManyToManyField(Officer)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)

    class Meta:
        db_table= 'Appointment'
        verbose_name_plural = 'Appointment'
