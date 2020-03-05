from django import forms
from cepf.models import Community, Officer

class FeedbackForm(forms.Form):
    attendance = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}),
                                    min_value=1, max_value=5, label='')

    reception = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}),
                                   min_value=1, max_value=5, label='')

    impact = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}),
                                min_value=1, max_value=5, label='')

    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),
                            label='Feedback Notes')

def communities():
    items = Community.objects.all().order_by('type')

    communities = tuple()

    for item in items:
        community = tuple((tuple((str(item.id), item.name))))
        communities += (community,)

    print(communities)

    return communities

def officers():
    items = Officer.objects.all().order_by('username')

    officers = tuple()

    for item in items:
        officer = tuple((str(item.id), item.get_full_name()))
        officers += (officer,)

    print(officers)

    return officers

class AssignForm(forms.Form):
    community = forms.ChoiceField(widget=forms.widgets.Select(), choices=communities(), label='')

    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'class': 'datepicker'}), label='')

    time = forms.TimeField(input_formats=['%I:%M %p'], widget=forms.widgets.TextInput(attrs={'class': 'timepicker'}), label='')

    officers = forms.MultipleChoiceField(widget=forms.widgets.SelectMultiple(), choices=officers(), label='')

    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='Extra Notes')

class CommunitiesForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),label='Community Name')

    type = forms.ChoiceField(widget=forms.widgets.Select(), choices=communities(), label='')

    location = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),label='Location')

    communication_channel = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),label='Telephone')

    engagement_period = forms.ChoiceField(widget=forms.widgets.Select(), choices=officers(), label='') #choices=officers() need to change to day, week and month

    engagement_period_multipler = forms.IntegerField(widget=forms.NumberInput(attrs={}),min_value=1, max_value=31, label='')
