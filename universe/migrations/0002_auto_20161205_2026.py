# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='locationtype',
            field=models.CharField(choices=[('HA', 'Hangar'), ('CA', 'Cantina'), ('MA', 'Market'), ('QU', 'Quest')], max_length=20),
        ),
        migrations.AlterField(
            model_name='planet',
            name='size',
            field=models.CharField(choices=[('TY', 'Tiny'), ('SM', 'Small'), ('ME', 'Medium'), ('LA', 'Large'), ('CO', 'Colossal')], default='ME', max_length=20),
        ),
    ]
