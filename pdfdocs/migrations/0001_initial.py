# Generated by Django 5.1.6 on 2025-03-18 06:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ums', '0005_alter_users_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('latex_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentSignature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature_data', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_valid', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ums.users')),
            ],
        ),
        migrations.CreateModel(
            name='GeneratedDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file_path', models.CharField(max_length=255)),
                ('context_data', models.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='created_documents', to='ums.users')),
                ('signed_by', models.ManyToManyField(through='pdfdocs.DocumentSignature', to='ums.users')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pdfdocs.documenttemplate')),
            ],
        ),
        migrations.AddField(
            model_name='documentsignature',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pdfdocs.generateddocument'),
        ),
    ]
