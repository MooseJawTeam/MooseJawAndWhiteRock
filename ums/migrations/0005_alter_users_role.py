# Generated by Django 5.1.6 on 2025-03-03 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ums', '0004_alter_users_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('Basicuser', 'Basic User')], default='Basicuser', max_length=100),
        ),
    ]
