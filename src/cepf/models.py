from django.db import models

class Community_Class(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Community(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    community_type = modles.ForeignKey(Community_Class)
    location = models.CharField(max_length=50)
    communication_channel = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    community = models.ForeignKey(Community)
    engagement_period = models.ForeignKey(Engagement_Period)
    engagement_period_multipler = modles.IntegerField()

class Engagement_Period(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

class Appointment_Feedback(models.Model):
    id = models.IntegerField(primary_key=True)
    start_rating1 = models.FloatField()
    start_rating2 = models.FloatField()
    start_rating3 = models.FloatField()
    notes = models.TextField()

class Officer(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    appointment_feedback = models.OneToOneField(Appointment_Feedback)
    officers = models.ManyToManyField(Officer)
    community = models.ForeignKey(Community)
