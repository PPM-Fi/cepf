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

    print(communities) #TODO: Remove

    return communities

def officers():
    items = Officer.objects.all().order_by('username')

    officers = tuple()

    for item in items:
        officer = tuple((str(item.id), item.get_full_name()))
        officers += (officer,)

    print(officers) #TODO: Remove

    return officers

class AssignForm(forms.Form):
    community = forms.ChoiceField(widget=forms.widgets.Select(), choices=communities(), label='')

    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'class': 'datepicker'}), label='')

    time = forms.TimeField(input_formats=['%I:%M %p'], widget=forms.widgets.TextInput(attrs={'class': 'timepicker'}), label='')

    officers = forms.MultipleChoiceField(widget=forms.widgets.SelectMultiple(), choices=officers(), label='')

    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='Extra Notes')

def community_types():
    communities = Community.objects.all()

    types = set()

    for community in communities:
        types.add(community.type)

    types_tuple = tuple()

    for type in types:
        type_tuple = tuple((type, type))
        types_tuple += (type_tuple,)

    print(types_tuple) #TODO: Remove

    return types_tuple

class CommunitiesForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='Community Name')

    type = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='Type')

    location = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='Location')

    communication_channel = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='Telephone')

    engagement_period = forms.ChoiceField(widget=forms.widgets.Select(), choices=(('Day', 'Day'), ('Week', 'Week'), ('Month', 'Month')), label='')

    engagement_period_multipler = forms.IntegerField(widget=forms.NumberInput(), min_value=1, max_value=31, label='')

class OfficerForm(forms.Form):
    first_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='')

    last_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='')

    badge_number = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), label='')

    email = forms.EmailField(widget=forms.EmailInput(), label='')

    password = forms.CharField(widget=forms.PasswordInput(), label='')
