# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 01:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('blog', '0002_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
