# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-05 17:13
from __future__ import unicode_literals

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("kolibriauth", "0014_auto_20190815_1421"),
    ]

    operations = [
        migrations.AddField(
            model_name="facilitydataset",
            name="registered",
            field=models.BooleanField(default=False),
        ),
    ]
