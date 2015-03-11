# -*- coding: utf-8 -*-

from rest_framework import serializers

from location.models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'name', 'tags', 'street', 'postal_code', 'city', 'country', 'longitude',
                  'latitude')
