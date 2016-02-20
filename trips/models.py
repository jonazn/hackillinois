from django.db import models
from django.contrib.auth.models import User

GENDERS = (("Male","Male"),("Female","Female"),("Other","Other"))
class Preference(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDERS, max_length=200)
    job = models.CharField(max_length=500)

    def __unicode__(self):
        return str(self.user) + "Preference"

class Trip(models.Model):
    origin = models.CharField(max_length=3 )
    destination = models.CharField(max_length=3)
    price = models.IntegerField()
    date = models.DateTimeField()
    hotel = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name="trip_owner")
    requester = models.ForeignKey(User, blank=True)
    private = models.BooleanField

class Request(models.Model):
    message = models.TextField()
    requester = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)




# Create your models here.
