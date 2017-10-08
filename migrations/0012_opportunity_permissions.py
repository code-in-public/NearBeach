# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 12:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0011_auto_20170911_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='opportunity_permissions',
            fields=[
                ('opportunity_permissions_id', models.AutoField(primary_key=True, serialize=False)),
                ('all_users', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunity_permissions_change_user', to=settings.AUTH_USER_MODEL)),
                ('customer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.customers')),
                ('groups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='NearBeach.groups')),
                ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.opportunity')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'opportunity_permission',
            },
        ),
    ]
