from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from cepf.models import Officer, Community, Feedback, Appointment

from datetime import date as d

@login_required(login_url='/auth/login/')
def calendar(request):
    context = {
        'today_date': d.today().strftime("%A, %d.%m.%Y"),
        'daily_assignments': [],
        'future_assignments': []
    }

    appointments = Appointment.objects.filter(
            officers__id=request.user.id
        ).order_by('date')

    for appointment in appointments:
        if appointment.date.date() == d.today():
            context['daily_assignments'].append(
                {
                    'name': appointment.community.name,
                    'time': appointment.date.strftime("%H:%M"),
                    'location': appointment.community.location,
                    'contact': appointment.community.communication_channel
                }
            )
        elif appointment.date.date() > d.today():
            context['future_assignments'].append(
                {
                    'name': appointment.community.name,
                    'time': appointment.date.strftime("%H:%M"),
                    'date': appointment.date.strftime("%A, %d.%m.%Y"),
                    'location': appointment.community.location,
                    'contact': appointment.community.communication_channel
                }
            )


    return render(request, 'calendar.html', context)

@login_required(login_url='/auth/login/')
def history(request):
    context = {
        'assignments': [],
    }

    appointments = Appointment.objects.filter(
            officers__id=request.user.id
        ).order_by('-date')

    for appointment in appointments:
        if appointment.date.date() < d.today():
            context['assignments'].append(
                {
                    'name': appointment.community.name,
                    'time': appointment.date.strftime("%H:%M"),
                    'date': appointment.date.strftime("%A, %d.%m.%Y"),
                    'location': appointment.community.location,
                    'contact': appointment.community.communication_channel
                }
            )

    return render(request, 'history.html', context)

@login_required(login_url='/auth/login/')
def analytics(request):
	template='analytics.html'
	return render(request, template)

@login_required(login_url='/auth/login/')
def communities(request):
	template='communities.html'
	return render(request, template)
