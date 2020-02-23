from django import forms

class FeedbackForm(forms.Form):
    attendance = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}),
                                    min_value=1, max_value=5, label='')

    reception = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}),
                                   min_value=1, max_value=5, label='')

    impact = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '1', 'min': '1', 'max': '5'}),
                                min_value=1, max_value=5, label='')

    notes = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),
                            label='Feedback Notes')
