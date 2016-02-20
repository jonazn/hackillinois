# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_trip_private'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='owner',
            field=models.ForeignKey(related_name='trips', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trip',
            name='requester',
            field=models.ForeignKey(related_name='requested', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
