from django import forms
from cepf.models import Post

class fbForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post
        fields = ('post',)
