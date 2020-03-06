from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from cepf.models import Officer, Community, Appointment, Feedback
from cepf.forms import FeedbackForm, AssignForm, CommunitiesForm, OfficerForm

from datetime import date as d
from datetime import datetime as dt

@login_required(login_url='/auth/login/')
def calendar(request):
    context = {
        'today_date': d.today().strftime("%A, %d.%m.%Y"),
        'past_assignments': [],
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

    past_appointments = Appointment.objects.filter(
            officers__id=request.user.id
        ).order_by('-date')

    labels = ['Finished', 'Unfinished']
    data = [0, 0]

    for past_appointment in past_appointments:
        if past_appointment.date.date() < d.today():
            context['past_assignments'].append(
                {
                    'name': past_appointment.community.name,
                    'time': past_appointment.date.strftime("%H:%M"),
                    'date': past_appointment.date.strftime("%A, %d.%m.%Y"),
                    'location': past_appointment.community.location,
                    'contact': past_appointment.community.communication_channel,
                    'is_completed': past_appointment.is_completed,
                    'id': past_appointment.id
                }
            )

        if past_appointment.is_completed:
            data[0] += 1
        else:
            data[1] += 1

    context['labels'] = labels
    context['data'] = data

    return render(request, 'calendar.html', context)

# @login_required(login_url='/auth/login/')
# def history(request):
#     context = {
#         'assignments': [],
#     }
#
#     appointments = Appointment.objects.filter(
#             officers__id=request.user.id
#         ).order_by('-date')
#
#     data = [0, 0]
#
#     for appointment in appointments:
#         if appointment.date.date() < d.today():
#             context['assignments'].append(
#                 {
#                     'name': appointment.community.name,
#                     'time': appointment.date.strftime("%H:%M"),
#                     'date': appointment.date.strftime("%A, %d.%m.%Y"),
#                     'location': appointment.community.location,
#                     'contact': appointment.community.communication_channel,
#                     'is_completed': appointment.is_completed,
#                     'id': appointment.id
#                 }
#             )
#
#             if appointment.is_completed:
#                 data[0] += 1
#             else:
#                 data[1] += 1
#
#     labels = ['Finished', 'Unfinished']
#
#     context['labels'] = labels
#     context['data'] = data
#
#     return render(request, 'history.html', context)

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

@login_required(login_url='/auth/login/')
@staff_member_required
def assign(request):
    if request.method == 'POST':
        print("posted\n") #TODO: Remove
        form = AssignForm(request.POST)
        print(form.data) #TODO: Remove
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            date_time = dt.combine(date, time)
            print(date_time) #TODO: Remove
            officers = []
            for officer in form.cleaned_data['officers']:
                officers.append(Officer.objects.get(id=int(officer)))
            community = Community.objects.get(id=int(form.cleaned_data['community']))
            assignment = Appointment(date=date_time,
                                     community=community,
                                     notes=form.cleaned_data['notes'])
            assignment.save()
            assignment.officers.set(officers)
            assignment.save()
            return HttpResponseRedirect('/assignments')
    else:
        form = AssignForm()

    return render(request, 'assign.html', {'form': form})


@login_required(login_url='/auth/login/')
@staff_member_required
def add_community(request):
    if request.method == 'POST':
        form = CommunitiesForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            location = form.cleaned_data['location']
            communication_channel = form.cleaned_data['communication_channel']
            engagement_period_multipler = form.cleaned_data['engagement_period_multipler']
            engagement_period = form.cleaned_data['engagement_period']
            community = Community(name=name,
                                  type=type,
                                  location=location,
                                  communication_channel=communication_channel,
                                  engagement_period_multipler=int(engagement_period_multipler),
                                  engagement_period=engagement_period)
            community.save()
            return HttpResponseRedirect('/communities')
    else:
        form = CommunitiesForm()

    return render(request, 'add_community.html', {'form': form})

@login_required(login_url='/auth/login/')
@staff_member_required
def add_officer(request):
    if request.method == 'POST':
        form = OfficerForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['badge_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            if form.cleaned_data['is_staff']:
                officer = Officer.objects.create_superuser(username=username,
                                                           first_name=first_name,
                                                           last_name=last_name,
                                                           email=email,
                                                           password=password)
            else:
                officer = Officer.objects.create_user(username=username,
                                                      first_name=first_name,
                                                      last_name=last_name,
                                                      email=email,
                                                      password=password)
            officer.save()
            return HttpResponseRedirect('/officers')
    else:
        form = OfficerForm()

    return render(request, 'add_officer.html', {'form': form})
