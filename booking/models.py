import datetime, random, uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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


class ShowModel(models.Model):
    theatre = models.ForeignKey(TheatreModel, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieModel, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.movie)+'-'+str(self.theatre)+'-'+str(self.date)+'-'+str(self.time)


class BookingModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_phone_number = PhoneField(help_text='Booker phone number')
    time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    show = models.ForeignKey(ShowModel, on_delete=models.CASCADE)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)+'-'+str(self.show.movie)+'-'+str(self.id)

# more features - seating model,
