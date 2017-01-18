# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='location',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='locationtype',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='moon',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='planet',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='planet',
            name='size',
            field=models.CharField(choices=[('TY', 'Tiny'), ('SM', 'Small'), ('ME', 'Medium'), ('LA', 'Large'), ('CO', 'Colossal')], max_length=20, default='ME'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
        migrations.AlterField(
            model_name='star',
            name='description',
            field=models.TextField(max_length=200, default=' '),
        ),
    ]
