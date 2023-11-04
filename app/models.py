from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
import datetime
import uuid

now = timezone.now()
naive_datetime = datetime.datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute, second=now.second)
aware_datetime = timezone.make_aware(naive_datetime, timezone=timezone.get_current_timezone())


class Property(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0)
    image = models.ImageField(upload_to='property_image/', null=True)
    rent_per_year = models.DecimalField(max_digits=20, decimal_places=0)
    lot_area = models.PositiveIntegerField()
    bed_rooms = models.PositiveIntegerField()
    bath_rooms = models.PositiveIntegerField()
    luggage = models.BooleanField(default=True)
    garage = models.PositiveIntegerField()
    floor_area = models.PositiveIntegerField()
    year_build = models.PositiveIntegerField()
    water = models.BooleanField(default=True)
    stories = models.PositiveIntegerField()
    roofing = models.CharField(max_length=200, choices=[('New', 'New'), ('Old', 'Old')])
    timestamp = models.DateTimeField(default=aware_datetime)

    def get_absolute_url(self):
        return reverse('app:property', args=[str(self.id)])

    def __str__(self):
        return self.name


class PropertyReview(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    review = models.TextField()
    ratings = models.PositiveIntegerField()
    timestamp = models.DateTimeField(default=aware_datetime)

    def get_absolute_url(self):
        return reverse('admin:review', kwargs={'id': self.id})

    def __str__(self):
        return self.name


class Agent(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    image = models.FileField(upload_to='agent_images/')
    name = models.CharField(max_length=255)
    properties = models.ManyToManyField(Property)
    timestamp = models.DateTimeField(default=aware_datetime)

    def __str__(self):
        return self.name