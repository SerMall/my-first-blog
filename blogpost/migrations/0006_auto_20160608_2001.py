# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 20:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0005_auto_20160608_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blogpost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogpost.Blogpost'),
        ),
    ]
