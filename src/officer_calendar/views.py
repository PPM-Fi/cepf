from django.shortcuts import render

def index(request):
	template='calendar/index.html'
	return render(request, template)

def base_layout(request):
	template='base.html'
	return render(request,template)
