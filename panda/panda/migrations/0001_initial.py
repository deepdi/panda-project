# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id_no', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('dob', models.DateField(verbose_name=b'Date created')),
            ],
        ),
    ]