# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('locationtype', models.CharField(max_length=20, choices=[(b'HA', b'Hangar'), (b'CA', b'Cantina'), (b'MA', b'Market'), (b'QU', b'Quest')])),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
                ('size', models.CharField(default=b'ME', max_length=20, choices=[(b'TY', b'Tiny'), (b'SM', b'Small'), (b'ME', b'Medium'), (b'LA', b'Large'), (b'CO', b'Colossal')])),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='planet',
            field=models.ForeignKey(to='universe.Planet'),
        ),
        migrations.AddField(
            model_name='item',
            name='resources',
            field=models.ManyToManyField(to='universe.Resource'),
        ),
    ]
