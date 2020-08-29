from rest_framework import generics, permissions, viewsets

from booking.models import (
    TheatreModel,
    MovieModel,
    BookingShowModel
)

from .serializer import (
    TheatreSerializer,
    MovieSerializer,
    BookingSerializer
)


class TheatreViewSets(viewsets.ModelViewSet):
    queryset =  TheatreModel.objects.all()
    serializer_class = TheatreSerializer
    permission_classes = (permissions.IsAuthenticated,)

class MovieViewSets(viewsets.ModelViewSet):
    queryset = MovieModel.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticated,)

class BookingViewSets(viewsets.ModelViewSet):
    queryset = BookingShowModel.objects.all()
    serializer_class = BookingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return 
