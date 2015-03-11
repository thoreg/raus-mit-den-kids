# -*- coding: utf-8 -*-
import googlemaps
from django.conf import settings


def get_geo_coords(*args):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    address_data = ' '.join(args)
    # print("address_data: {}".format(address_data))

    geocode_result = gmaps.geocode(address_data)
    if not geocode_result:
        return None, None

    # print('geocode_result: {}'.format(geocode_result))

    latitude = geocode_result[0]['geometry']['location']['lat']
    longitude = geocode_result[0]['geometry']['location']['lng']

    return float(latitude), float(longitude)
