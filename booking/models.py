import datetime, random, uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.timezone import now


from phone_field import PhoneField


class TheatreModel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class MovieModel(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    rating = models.IntegerField(default=5)
    language = models.CharField(max_length=50, default='Hindi')
    director = models.CharField(max_length=50)
    run_length = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class BookingShowModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_phone_number = PhoneField(help_text='Booker phone number')
    theatre = models.ForeignKey(TheatreModel, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    expired = models.BooleanField(default=False)
    issued_date = models.DateField(default=now)
    issued_time = models.TimeField(default=now)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.id)+'-'+str(self.user.username)

# more features - seating model, Booking show model can be broken into two more models(show booking and booking model)
