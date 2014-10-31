from django.db import models
from taggit.managers import TaggableManager

from django_countries.fields import CountryField


class Address(models.Model):
    name = models.CharField(max_length=255)
    tags = TaggableManager()
    modification_date = models.DateTimeField(auto_now=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    # submitter?

    street = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = CountryField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)


class Link(models.Model):
    href = models.CharField(max_length=1024)
    address = models.ForeignKey(Address)
