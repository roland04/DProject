# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='current_hitpoints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='fame',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='max_hitpoints',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
    ]
