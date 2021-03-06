# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-20 03:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('headline', models.CharField(max_length=70)),
                ('content', models.TextField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Reporter')),
            ],
        ),
    ]
