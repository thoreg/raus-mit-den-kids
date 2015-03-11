# -*- coding: utf-8 -*-
from django.conf.urls import include, patterns
from rest_framework import routers

from location.viewsets import AddressViewSet

router = routers.DefaultRouter()

router.register(r'addresses', AddressViewSet)

urlpatterns = patterns('', (r'^', include(router.urls)))
