from django.shortcuts import render
from .models import Club
from django.http import HttpResponse


# Create your views here.
def home_page(request):
    return render(request, 'basic/home_page.html')


def club_page(request, slug):
    t = False
    slug = slug.lower()
    clubs = Club.objects.all()
    for i in clubs:
        if slug == i.club_name.lower():
            t = True
            break
    if t:
        return render(request, 'basic/club_page.html', {'club': i})
    else:
        return HttpResponse('<h1>Club does not exist !!</h1><br><a href="/basic/">Go Back</a>')
