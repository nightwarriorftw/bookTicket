from django.contrib import admin
from .models import (
    MovieModel,
    TheatreModel,
    ShowModel,
    BookingModel
)

admin.site.register(TheatreModel)
admin.site.register(MovieModel)
admin.site.register(ShowModel)
admin.site.register(BookingModel)
