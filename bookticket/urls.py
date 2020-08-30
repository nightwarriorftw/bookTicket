from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/api/v1/', include('accounts.api.urls', namespace='accounts')),
    path('book/api/v1/', include('booking.api.urls', namespace='book')),
]
