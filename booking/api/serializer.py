from rest_framework import serializers

from django.contrib.auth.models import User

from booking.models import (
    TheatreModel,
    MovieModel,
    BookingShowModel
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


class BookingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    theatre = TheatreSerializer()
    movie = MovieSerializer()

    class Meta:
        model = BookingShowModel
        fields = ('user', 'booking_phone_number', 'time', 'date',
                  'theatre', 'movie', 'expired')

    def create(self, validated_data):
        movie = validated_data.pop('movie')
        theatre = validated_data.pop('theatre')
        userObj = self.context['request'].user
        
        movieObj, created = MovieModel.objects.get_or_create(**movie)

        theatreObj, created = TheatreModel.objects.get_or_create(**theatre)

        return BookingShowModel.objects.create(user=userObj, movie=movieObj, theatre=theatreObj, **validated_data)
