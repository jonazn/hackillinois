# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=200, choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Other', b'Other')])),
                ('job', models.CharField(max_length=500)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('requester', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origin', models.CharField(max_length=3)),
                ('destination', models.CharField(max_length=3)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('hotel', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(related_name='trip_owner', to=settings.AUTH_USER_MODEL)),
                ('requester', models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='trip',
            field=models.ForeignKey(to='trips.Trip'),
        ),
    ]
