from django.shortcuts import render, get_object_or_404
from clubs.models import Club
from posts.models import Post
from events.models import Event
# Create your views here.


def home_page(request):
    clubs = Club.objects.all()
    events = Event.objects.all()
    posts = Post.objects.all()
    return render(request, 'events/home_page.html', {'Clubs': clubs, 'Posts': posts, 'Events': events})


def event_detail(request, pk2):
    clubs = Club.objects.all()
    events = Event.objects.all()
    event = get_object_or_404(Post, pk=pk2)
    return render(request, 'events/event_detail.html', {'Clubs': clubs, 'event': event, 'Events': events})
