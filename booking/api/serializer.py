from rest_framework import serializers

from django.contrib.auth.models import User

from booking.models import (
    TheatreModel,
    MovieModel,
    ShowModel,
    BookingModel
)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class TheatreSerializer(serializers.ModelSerializer):

    class Meta:
        model = TheatreModel
        fields = ('id', 'name', 'address')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieModel
        fields = ('id', 'name', 'release_date', 'rating',
                  'language', 'director', 'run_length')


class ShowSerializer(serializers.ModelSerializer):
    theatre = TheatreSerializer()
    movie = MovieSerializer()

    class Meta:
        model = ShowModel
        fields = ('theatre', 'movie', 'date', 'time')


class BookingSerializer(models.Model):
    user = UserSerializer()
    show = ShowSerializer()

    class Meta:
        model = BookingModel
        fields = ('user', 'booking_phone_number', 'time',
                  'updated_time', 'show', 'expired')
