# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 15:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelapp', '0009_auto_20170705_1526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stay', models.IntegerField()),
                ('food', models.IntegerField()),
                ('travelling_charges', models.IntegerField()),
                ('offer_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelling_date', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('no_of_persons', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default=None, max_length=150, null=True)),
                ('description', models.CharField(max_length=1000)),
                ('no_of_days', models.IntegerField()),
                ('ratings', models.FloatField(blank=True, default=None, null=True)),
                ('category', models.CharField(max_length=30)),
                ('mapid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.PlaceMap')),
                ('stateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.State')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('packageid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.Packages')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='packageid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.Packages'),
        ),
        migrations.AddField(
            model_name='booking',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='amount',
            name='packageid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelapp.Packages'),
        ),
    ]
