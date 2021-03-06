from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar, name='calendar'),
    # path('history', views.history, name='history'),
    path('add_feedback/<int:id>/<str:back>/', views.add_feedback, name='add_feedback'),
    path('assignments', views.assignments, name='assignments'),
    path('communities', views.communities, name='communities'),
    path('officers', views.officers, name='officers'),
    path('assign', views.assign, name='assign'),
    path('add_community', views.add_community, name='add_community'),
    path('add_officer', views.add_officer, name='add_officer'),
    path('analytics', views.analytics, name='analytics'),
]
