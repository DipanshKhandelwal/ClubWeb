from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^clubs/(?P<slug>[-\w\d]+)/$', views.club_page, name='club_page'),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^events/(?P<pk2>\d+)/$', views.event_detail, name='event_detail'),

]
