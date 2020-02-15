from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Officer#, Community_Class, Community, Appointment, Appointment_Feedback, Engagement_Period

admin.site.register(Officer, UserAdmin)

# admin.site.register(Community_Class)
# admin.site.register(Community)
# admin.site.register(Appointment)
# admin.site.register(Appointment_Feedback)
# admin.site.register(Engagement_Period)
