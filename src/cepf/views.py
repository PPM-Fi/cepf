from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from cepf.models import Officer, Community, Appointment, Feedback
from cepf.forms import FeedbackForm

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
                    'contact': appointment.community.communication_channel,
                    'is_completed': appointment.is_completed,
                    'id': appointment.id
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

    data = [0, 0]

    for appointment in appointments:
        if appointment.date.date() < d.today():
            context['assignments'].append(
                {
                    'name': appointment.community.name,
                    'time': appointment.date.strftime("%H:%M"),
                    'date': appointment.date.strftime("%A, %d.%m.%Y"),
                    'location': appointment.community.location,
                    'contact': appointment.community.communication_channel,
                    'is_completed': appointment.is_completed,
                    'id': appointment.id
                }
            )

            if appointment.is_completed:
                data[0] += 1
            else:
                data[1] += 1

    labels = ['Finished', 'Unfinished']

    context['labels'] = labels
    context['data'] = data

    return render(request, 'history.html', context)

@login_required(login_url='/auth/login/')
def add_feedback(request, id, back):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = Feedback(attendance=form.cleaned_data['attendance'],
                                reception=form.cleaned_data['reception'],
                                impact=form.cleaned_data['impact'],
                                notes=form.cleaned_data['notes'])
            feedback.save()
            appointment = Appointment.objects.get(id=id)
            appointment.feedback = feedback
            appointment.is_completed = True
            appointment.save()
            if back == 'calendar':
                return HttpResponseRedirect('/')
            elif back == 'history':
                return HttpResponseRedirect('/history')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})

@login_required(login_url='/auth/login/')
@staff_member_required
def assignments(request):
    items = Appointment.objects.all().order_by('date')

    return render(request, 'assignments.html', {'items': items})

@login_required(login_url='/auth/login/')
@staff_member_required
def communities(request):
    items = Community.objects.all().order_by('type')

    return render(request, 'communities.html', {'items': items})

@login_required(login_url='/auth/login/')
@staff_member_required
def officers(request):
    items = Officer.objects.all().order_by('username')

    return render(request, 'officers.html', {'items': items})
