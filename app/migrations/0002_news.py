# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('url', models.URLField(unique=True)),
                ('url_image', models.URLField(unique=True)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]
