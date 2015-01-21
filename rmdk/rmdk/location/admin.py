# -*- coding: utf-8 -*-
from django.contrib import admin

from rmdk.location.forms import AddressAdminForm
from rmdk.location.models import Address, Link


class LinkInline(admin.TabularInline):
    model = Link


class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'postal_code', 'city')
    inlines = [
        LinkInline,
    ]
    form = AddressAdminForm


admin.site.register(Address, AddressAdmin)
