from django.db import models
from django.utils import timezone
# Create your models here.
CLUB_NAMES = (
    ('ArtClub', 'ART CLUB'),
    ('DanceClub', 'DANCE CLUB'),
    ('MusicClub', 'MUSIC CLUB'),
    ('CodingClub', 'CODING CLUB'),
    ('GamingClub', 'GAMING CLUB'),
    ('PhotographyClub', 'PHOTOGRAPHY CLUB'),
)

class Post(models.Model):
    club_name = models.CharField(max_length=10, choices=CLUB_NAMES)
    title = models.CharField(max_length=120)
    information = models.TextField()
    post_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title