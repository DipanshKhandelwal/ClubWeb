from django import forms
from .models import Post


class Post(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['club_name', 'title', 'information']


class Event(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'information', 'time']
