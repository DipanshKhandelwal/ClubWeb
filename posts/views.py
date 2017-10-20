from django.shortcuts import render, get_object_or_404
from clubs.models import Club
from posts.models import Post
from events.models import Event
# Create your views here.


def home_page(request):
    clubs = Club.objects.all()
    events = Event.objects.all()
    posts = Post.objects.all()
    return render(request, 'posts/home_page.html', {'Clubs': clubs, 'Posts': posts, 'Events': events})


def post_detail(request, pk):
    clubs = Club.objects.all()
    events = Event.objects.all()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'Clubs': clubs, 'post': post, 'Events': events})
