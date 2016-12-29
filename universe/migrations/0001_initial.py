# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ItemResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(to='universe.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Moon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b' ', max_length=200)),
                ('size', models.CharField(default=b'ME', max_length=20, choices=[(b'TY', b'Tiny'), (b'SM', b'Small'), (b'ME', b'Medium'), (b'LA', b'Large'), (b'CO', b'Colossal')])),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(default=b' ', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='planet',
            name='star',
            field=models.ForeignKey(to='universe.Star'),
        ),
        migrations.AddField(
            model_name='moon',
            name='planet',
            field=models.ForeignKey(to='universe.Planet'),
        ),
        migrations.AddField(
            model_name='location',
            name='locationtype',
            field=models.ForeignKey(to='universe.LocationType'),
        ),
        migrations.AddField(
            model_name='location',
            name='planet',
            field=models.ForeignKey(to='universe.Planet'),
        ),
        migrations.AddField(
            model_name='itemresource',
            name='resource',
            field=models.ForeignKey(to='universe.Resource'),
        ),
        migrations.AddField(
            model_name='item',
            name='resources',
            field=models.ManyToManyField(to='universe.Resource', through='universe.ItemResource'),
        ),
    ]
