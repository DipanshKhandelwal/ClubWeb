from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^artclub/', views.art_club, name='art_club'),
    url(r'^danceclub/', views.dance_club, name='_dance_club'),

]