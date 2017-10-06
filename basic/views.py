from django.shortcuts import render, get_object_or_404
from .models import Club, Post, Event


# Create your views here.
def home_page(request):
    clubs = Club.objects.all()
    events = Event.objects.all()
    posts = Post.objects.all()
    return render(request, 'basic/home_page.html', {'Clubs': clubs, 'Posts': posts, 'Events': events})


def post_detail(request, pk):
    clubs = Club.objects.all()
    events = Event.objects.all()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'basic/post_detail.html', {'Clubs': clubs, 'post': post, 'Events': events})


def event_detail(request, pk2):
    clubs = Club.objects.all()
    events = Event.objects.all()
    event = get_object_or_404(Post, pk=pk2)
    return render(request, 'basic/event_detail.html', {'Clubs': clubs, 'event': event, 'Events': events})


def club_page(request, slug):
    x = Club.objects.all()
    events = Event.objects.all()
    t = False
    slug = slug.lower()
    clubs = Club.objects.all()
    for i in clubs:
        if slug == i.club_name.lower():
            t = True
            break
    if t:
        return render(request, 'basic/club_page.html', {'club': i, 'Clubs': x, 'Events': events})
    else:
        return render(request, 'basic/error404.html', {'Clubs': x, 'Events': events})

