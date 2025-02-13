# Generated by Django 3.1.2 on 2021-01-23 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0004_auto_20201114_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='change_task',
            name='is_downtime',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='change_task',
            name='change_task_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='change_task_block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('blocked_change_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocked_change_task', to='NearBeach.change_task')),
                ('change_task_blocks', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_task_blocks', to='NearBeach.change_task')),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_task_block_change_user', to=settings.AUTH_USER_MODEL)),
                ('creation_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='change_task_block_creation_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'change_task_block',
            },
        ),
    ]
