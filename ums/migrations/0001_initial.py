# Generated by Django 5.1.6 on 2025-02-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Basicuser', 'Basic User')], default='Basicuser', max_length=100)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]
