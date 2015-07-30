# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0007_auto_20150730_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='country_name',
            field=models.CharField(unique=True, max_length=200),
            preserve_default=True,
        ),
    ]
