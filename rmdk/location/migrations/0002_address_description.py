# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='description',
            field=models.CharField(default='', max_length=2048),
            preserve_default=False,
        ),
    ]
