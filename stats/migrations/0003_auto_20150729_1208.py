# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20150713_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='has_death_penalty',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='has_employment_protection',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='has_hate_crime_protection',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='has_marriage_recognition',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='country',
            name='is_illegal',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
