from django.shortcuts import render, get_object_or_404
from .models import Club, Post


# Create your views here.
def home_page(request):
    clubs = Club.objects.all()
    posts = Post.objects.all()
    return render(request, 'basic/home_page.html', {'Clubs': clubs, 'Posts': posts})


def post_detail(request, pk):
    clubs = Club.objects.all()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'basic/post_detail.html', {'Clubs': clubs, 'post': post})


def club_page(request, slug):
    x = Club.objects.all()
    t = False
    slug = slug.lower()
    clubs = Club.objects.all()
    for i in clubs:
        if slug == i.club_name.lower():
            t = True
            break
    if t:
        return render(request, 'basic/club_page.html', {'club': i, 'Clubs': x})
    else:
        return render(request, 'basic/error404.html', {'Clubs': x})

