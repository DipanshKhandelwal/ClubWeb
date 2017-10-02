from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'basic/home_page.html')


def club_page(request, slug):
    return render(request, 'basic/club_page.html', {'clubname': slug})
