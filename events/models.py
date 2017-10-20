from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=120)
    information = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title + 'at' + str(self.time)
