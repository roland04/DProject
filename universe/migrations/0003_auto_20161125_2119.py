# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0002_auto_20161125_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('locationtype', models.CharField(choices=[('HA', 'Hangar'), ('CA', 'Cantina')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='planet',
            name='size',
            field=models.CharField(choices=[('TY', 'Tiny'), ('SM', 'Small'), ('ME', 'Medium'), ('LA', 'Large'), ('CO', 'Colossal')], max_length=20, default='ME'),
        ),
        migrations.AddField(
            model_name='location',
            name='planet',
            field=models.ForeignKey(to='universe.Planet'),
        ),
    ]
