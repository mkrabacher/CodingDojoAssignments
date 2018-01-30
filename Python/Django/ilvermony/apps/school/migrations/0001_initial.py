# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
                ('start', models.TimeField(verbose_name='%H:%M')),
                ('end', models.TimeField(verbose_name='%H:%M')),
                ('spots', models.IntegerField()),
                ('total_spots', models.IntegerField()),
                ('students', models.ManyToManyField(related_name='classes', to='users.User')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teaching', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('rated_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_given', to='school.Class')),
                ('rater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rated_classes', to='users.User')),
            ],
        ),
    ]