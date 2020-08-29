from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import (
    TheatreViewSets,
    MovieViewSets,
    BookingViewSets,
    TicketsListAPI,
)

app_name='booking'

router = DefaultRouter()
router.register('theatre', TheatreViewSets, basename='theatre')
router.register('movie', MovieViewSets, basename='movie')
router.register('booking', BookingViewSets, basename='booking')

urlpatterns = router.urls

urlpatterns+=[
    path('tickets/', TicketsListAPI.as_view(), name='tickets'),
]
