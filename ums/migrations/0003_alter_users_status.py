# Generated by Django 5.1.6 on 2025-02-28 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0002_rename_is_active_users_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='status',
            field=models.CharField(default='Active', max_length=10),
        ),
    ]
