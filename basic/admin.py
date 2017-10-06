from django.contrib import admin
from .models import Post, Club, ClubMember, Event
# Register your models here.

my_models = [Post, Club, ClubMember, Event]
admin.site.register(my_models)
