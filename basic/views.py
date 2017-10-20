from django.shortcuts import render
from clubs.models import Club
from events.models import Event
from posts.models import Post


# Create your views here.
def home_page(request):
    clubs = Club.objects.all()
    events = Event.objects.all()
    posts = Post.objects.all()
    return render(request, 'basic/home_page.html', {'Clubs': clubs, 'Posts': posts, 'Events': events})
