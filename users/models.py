from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

now = timezone.now()
naive_datetime = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
aware_datetime = timezone.make_aware(naive_datetime, timezone=timezone.get_current_timezone())


class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    date_joined = models.DateTimeField(default=aware_datetime)
