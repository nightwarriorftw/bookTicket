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
        fields = ('id', 'user', 'booking_phone_number', 'show_time', 'show_date',
                  'theatre', 'movie', 'expired', 'created')

    def create(self, validated_data):
        movie = validated_data.pop('movie')
        theatre = validated_data.pop('theatre')
        userObj = self.context['request'].user

        movieObj, created = MovieModel.objects.get_or_create(**movie)

        theatreObj, created = TheatreModel.objects.get_or_create(**theatre)

        ticket = BookingShowModel.objects.create(
            user=userObj, movie=movieObj, theatre=theatreObj, **validated_data)
        ticket.save()
        return ticket

    def update(self, instance, validated_data):
        instance.booking_phone_number = validated_data.get(
            'booking_phone_number', instance.booking_phone_number)
        instance.show_time = validated_data.get('show_time', instance.show_time)
        instance.show_date = validated_data.get('show_date', instance.show_date)
        instance.created = validated_data.get(
            'created', instance.created)
        instance.expired = validated_data.get('expired', instance.expired)

        if(validated_data.get('theatre')):
            try:
                theatre = TheatreModel.objects.get(
                    id=validated_data.get('theatre')['name'])
                instance.theatre.id = theatre.id
                instance.theatre.name = theatre.name
                instance.theatre.address = theatre.address
            except:
                raise serializers.ValidationError('Theatre does not exixts')
        if(validated_data.get('movie')):
            try:
                movie = MovieModel.objects.get(
                    name=validated_data.get('movie')['name'])
                instance.movie = movie

            except:
                raise serializers.ValidationError('Movie does not exixts')

        instance.save()
        return instance
