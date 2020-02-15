from django.db import models
from django.contrib.auth.models import AbstractUser

class Officer(AbstractUser):
    pass

# class Community_Class(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     class Meta:
#         verbose_name_plural = "Community_Classes"
#
# class Engagement_Period(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     class Meta:
#         verbose_name_plural = "Engagement_Periods"
#
# class Community(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=50)
#     community_type = models.ForeignKey(Community_Class, on_delete=models.CASCADE)
#     location = models.CharField(max_length=50)
#     communication_channel = models.CharField(max_length=50)
#     phone_number = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     engagement_period = models.ForeignKey(Engagement_Period, on_delete=models.CASCADE)
#     engagement_period_multipler = models.IntegerField()
#     class Meta:
#         verbose_name_plural = "Communities"
#
# class Appointment_Feedback(models.Model):
#     id = models.IntegerField(primary_key=True)
#     start_rating1 = models.FloatField()
#     start_rating2 = models.FloatField()
#     start_rating3 = models.FloatField()
#     notes = models.TextField()
#     class Meta:
#         verbose_name_plural = "Appointments_Feedback"
#
# class Appointment(models.Model):
#     id = models.IntegerField(primary_key=True)
#     date = models.DateTimeField()
#     appointment_feedback = models.OneToOneField(Appointment_Feedback, on_delete=models.CASCADE)
#     officers = models.ManyToManyField(Officer)
#     community = models.ForeignKey(Community, on_delete=models.CASCADE)
