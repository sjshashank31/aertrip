from django.db import models

# Create your models here.


class Place(models.Model):
    place_name = models.CharField(max_length=100)

    def __str__(self):
        return self.place_name


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.event_name




