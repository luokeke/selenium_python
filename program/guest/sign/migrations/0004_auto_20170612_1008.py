# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-12 02:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0003_delete_ni'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='guest',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
    ]
