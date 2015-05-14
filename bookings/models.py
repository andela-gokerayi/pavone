from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100, unique=True)
    event_color = models.CharField(max_length=100, unique=True)
    event_venue = models.CharField(max_length=100, unique=True)
    date_of_event = models.DateField()

    def __unicode__(self): 
        return '{}'.format(self.name)