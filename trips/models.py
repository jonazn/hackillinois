from django.db import models
from django.contrib.auth.models import User

class Preference(models.Model):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"
    GENDERS = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )
    user = models.OneToOneField(User)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDERS, max_length=200)
    job = models.CharField(max_length=500)

    def __unicode__(self):
        return str(self.user) + " Preference"

class Trip(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    price = models.IntegerField()
    date = models.DateTimeField()
    hotel = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name="trips")
    requester = models.ForeignKey(User, related_name="requested", blank=True)
    private = models.BooleanField(default=False)

class Request(models.Model):
    message = models.TextField()
    requester = models.ForeignKey(User)
    trip = models.ForeignKey(Trip)




# Create your models here.
