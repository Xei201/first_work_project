# Generated by Django 4.1.6 on 2023-02-13 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import integration.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WebroomTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=200)),
                ('roomid', models.CharField(max_length=200)),
                ('webinarId', models.CharField(max_length=200)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('start_upload', models.BooleanField(default=False)),
                ('result_upload', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViewersImport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('view', models.CharField(max_length=200)),
                ('buttons', models.CharField(max_length=200)),
                ('banners', models.CharField(max_length=200)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('import_to_gk', models.BooleanField(default=False)),
                ('webroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integration.webroomtransaction')),
            ],
            options={
                'ordering': ['create'],
            },
        ),
        migrations.CreateModel(
            name='TokenImport',
            fields=[
                ('token', models.UUIDField(default=integration.models.get_default_field_token, primary_key=True, serialize=False)),
                ('token_gk', models.CharField(default=None, max_length=100, null=True)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['create'],
            },
        ),
    ]
