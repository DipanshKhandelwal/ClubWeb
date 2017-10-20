from django.shortcuts import render
from clubs.models import Club, ClubMember
from posts.models import Post
from events.models import Event
# Create your views here.


def home_page(request):
    clubs = Club.objects.all()
    events = Event.objects.all()
    posts = Post.objects.all()
    return render(request, 'clubs/home_page.html', {'Clubs': clubs, 'Posts': posts, 'Events': events})


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
        members = ClubMember.objects.filter(club=i)
        return render(request, 'clubs/club_page.html', {'club': i, 'Clubs': x, 'Events': events, 'members': members})
    else:
        return render(request, 'basic/error404.html', {'Clubs': x, 'Events': events})
