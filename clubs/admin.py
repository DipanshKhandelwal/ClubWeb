from django.contrib import admin
from .models import Club, ClubMember
# Register your models here.

my_models = [Club, ClubMember]
admin.site.register(my_models)
