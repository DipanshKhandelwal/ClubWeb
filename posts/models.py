from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    club_name = models.CharField(max_length=20, choices=CLUB_NAMES)
    title = models.CharField(max_length=120)
    information = models.TextField()
    post_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.club_name + '--' + self.title
