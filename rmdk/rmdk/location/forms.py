# -*- coding: utf-8 -*-
from django import forms

from rmdk.location.models import Address


class AddressAdminForm(forms.ModelForm):
    class Meta:
        model = Address
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
