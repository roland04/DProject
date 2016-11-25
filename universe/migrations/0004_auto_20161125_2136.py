# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universe', '0003_auto_20161125_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='locationtype',
            field=models.CharField(max_length=20, choices=[('HA', 'Hangar'), ('CA', 'Cantina'), ('MA', 'Market'), ('QU', 'Quest')]),
        ),
        migrations.AddField(
            model_name='item',
            name='resources',
            field=models.ManyToManyField(to='universe.Resource'),
        ),
    ]
