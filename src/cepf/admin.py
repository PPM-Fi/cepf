from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Officer, Community, Appointment, Feedback

admin.site.register(Officer, UserAdmin)
admin.site.register(Community)
admin.site.register(Feedback)
admin.site.register(Appointment)
