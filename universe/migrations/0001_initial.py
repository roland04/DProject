# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('size', models.CharField(default='ME', choices=[('TY', 'Tiny'), ('SM', 'Small'), ('ME', 'Medium'), ('LA', 'Large'), ('CO', 'Colossal')], max_length=200)),
            ],
        ),
    ]
