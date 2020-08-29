from rest_framework.routers import DefaultRouter
from .views import (
    TheatreViewSets,
    MovieViewSets,
    BookingViewSets
)

app_name='booking'

router = DefaultRouter()
router.register('theatre', TheatreViewSets, basename='theatre')
router.register('movie', MovieViewSets, basename='movie')
router.register('booking', BookingViewSets, basename='booking')

urlpatterns = router.urls
