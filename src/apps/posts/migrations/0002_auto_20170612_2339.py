# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-13 03:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-actualizado']},
        ),
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
