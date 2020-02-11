from django.contrib import admin

from .models import Community_Class, Community, Appointment, Appointment_Feedback, Officer, Engagement_Period

admin.site.register(Community_Class)
admin.site.register(Community)
admin.site.register(Appointment)
admin.site.register(Appointment_Feedback)
admin.site.register(Officer)
admin.site.register(Engagement_Period)
