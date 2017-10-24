from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='events_home_page'),
    url(r'^(?P<pk2>\d+)/$', views.event_detail, name='event_detail'),
]
