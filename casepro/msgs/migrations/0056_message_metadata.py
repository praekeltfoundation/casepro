# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-08 14:51
from __future__ import unicode_literals

import django.contrib.postgres.fields.hstore
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0055_auto_20170117_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='metadata',
            field=django.contrib.postgres.fields.hstore.HStoreField(blank=True, default={}, help_text='Metadata for the received message.', null=True),
        ),
    ]
