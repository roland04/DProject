# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='description',
            field=models.TextField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(default=' ', max_length=200),
        ),
    ]
