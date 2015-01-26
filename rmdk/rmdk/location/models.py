# -*- coding: utf-8 -*-
from django.contrib.gis.db import models
from django_countries.fields import CountryField
from taggit.managers import TaggableManager

from rmdk.location.services import get_geo_coords


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

    description = models.CharField(max_length=2048)

    def __str__(self):
        return self.name

    def save(self, **kwargs):
        if not self.latitude:
            self.latitude, self.longitude = get_geo_coords(self.street, self.postal_code)

        super(Address, self).save(**kwargs)


class Link(models.Model):
    href = models.CharField(max_length=1024)
    address = models.ForeignKey(Address)
