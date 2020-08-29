from django.contrib import admin
from .models import (
    MovieModel,
    TheatreModel,
    BookingShowModel
)

admin.site.register(TheatreModel)
admin.site.register(MovieModel)
admin.site.register(BookingShowModel)
