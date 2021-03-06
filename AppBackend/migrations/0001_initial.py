# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-21 00:11
from __future__ import unicode_literals

import AppBackend.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.TextField()),
                ('longtitude', models.TextField()),
                ('text', models.TextField()),
                ('picture', models.ImageField(upload_to=AppBackend.models.get_image_path)),
                ('title', models.TextField()),
                ('name', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
