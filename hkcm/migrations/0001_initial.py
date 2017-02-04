# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cmdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuetime', models.DateTimeField(null=True)),
                ('location', models.CharField(max_length=50)),
                ('crime', models.CharField(max_length=50)),
                ('crimecat', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('title', models.CharField(max_length=50)),
                ('URL', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='cmdata',
            unique_together=set([('title', 'location', 'crime')]),
        ),
    ]