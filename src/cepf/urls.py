from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    path('analytics', views.analytics, name='analytics'),
    path('communities', views.communities, name='communities'),
    path('feedback', views.feedback, name='feedback'),
]
