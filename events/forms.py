from django import forms
from .models import Post


class Event(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'information', 'time']
