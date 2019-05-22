# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_schedule'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
                ('individual', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer_1', models.CharField(max_length=250)),
                ('answer_2', models.CharField(max_length=250)),
                ('answer_3', models.CharField(max_length=250)),
                ('answer_4', models.CharField(max_length=250)),
                ('answer_5', models.CharField(max_length=250)),
                ('correct_answer', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RetiredNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=250)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamAward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='awards',
            field=models.ManyToManyField(to='app.PlayerAward'),
        ),
        migrations.AddField(
            model_name='team',
            name='awards',
            field=models.ManyToManyField(to='app.TeamAward'),
        ),
        migrations.AddField(
            model_name='team',
            name='retired_numbers',
            field=models.ManyToManyField(to='app.RetiredNumber'),
        ),
    ]