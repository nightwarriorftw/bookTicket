from rest_framework import generics, permissions, viewsets

from django.shortcuts import get_object_or_404

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


class TicketsListAPI(generics.RetrieveAPIView):
    permissions_classes = [permissions.IsAuthenticated]
    serializer_class = BookingSerializer

    def get_object(self):
        print(self.request.data)
        obj = get_object_or_404(BookingShowModel, issued_time=self.request.data['issued_time'])
        return obj
