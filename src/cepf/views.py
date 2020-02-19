from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from cepf.models import Officer, Community, Appointment

from datetime import date as d

from cepf.form import fbForm

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

@login_required(login_url='/auth/login/')
def feedback(request):
    	template='feedback.html'
    	return render(request, template)

class ClassName(object):

        def get(self, request):
            template_name='feedback.html'
            form = fbForm()
            return render(request, self.template_name, {'form': form})

        def post(self, request):
            form = fbForm(request.POST)
            if form.is_valid():
                form.saved(commit=False)
                post.User = request.user
                post.save()

                text = form.cleaned_data['post']
                #form = fbForm()
                #return redirect(redirectCal)

            args = {'form': form, 'text': text}
            return render(request, self.template_name, args)
