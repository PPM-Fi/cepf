from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def calendar(request):
	template='calendar.html'
	return render(request, template)

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
