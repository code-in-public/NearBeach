# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 08:42
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0005_permission_set_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_content',
            name='email_content',
            field=tinymce.models.HTMLField(verbose_name='email_content'),
        ),
    ]
