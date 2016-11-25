# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
