# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-23 06:12
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_raw_name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('book_simple_name', models.CharField(max_length=200)),
                ('book_url', models.CharField(default='http://', max_length=200)),
                ('book_img', models.CharField(default='http://', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=10000)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=10000)),
                ('find_page', models.IntegerField()),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('book_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kindle.Book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=10000)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('mark_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kindle.Mark')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='mark_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kindle.Mark'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
