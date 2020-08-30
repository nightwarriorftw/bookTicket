import os
from django.conf import settings
from .models import BookingShowModel
from datetime import datetime, timedelta

def mark_expired_ticket():
    try:
        time_threshold = datetime.now() - timedelta(hours=8)
        queryset = BookingShowModel.objects.filter(created__lt=time_threshold)
        queryset.delete() # delete queryset
        f = open(os.path.join(settings.MEDIA_ROOT, 'log.txt'), 'a')
        f.write(' deleted \n')
        f.close()
    except:
        f = open(os.path.join(settings.MEDIA_ROOT, 'log.txt'), 'a')
        f.write(' Logging !! ')
        f.close()
