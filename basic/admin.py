from django.contrib import admin
from .models import Post, Club, ClubMember
# Register your models here.

my_models = [Post, Club, ClubMember]
admin.site.register(my_models)
