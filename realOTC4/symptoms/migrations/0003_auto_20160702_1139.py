# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-02 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symptoms', '0002_symptoms_sym'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('Cough', models.BooleanField()),
                ('Fever', models.BooleanField()),
                ('Runny_Nose', models.BooleanField()),
                ('Nasal_Congestion', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='symptoms',
            name='sym',
        ),
    ]
