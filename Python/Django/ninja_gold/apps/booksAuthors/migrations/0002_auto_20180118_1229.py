# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-18 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booksAuthors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
