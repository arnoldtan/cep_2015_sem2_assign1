# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country_name', models.CharField(max_length=200)),
                ('has_death_penalty', models.BooleanField()),
                ('has_imprisonment', models.BooleanField()),
                ('has_employment_protection', models.BooleanField()),
                ('has_hate_crime_protection', models.BooleanField()),
                ('has_marriage_recognition', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
