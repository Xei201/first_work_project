# Generated by Django 4.1.6 on 2023-02-08 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_create_date_alter_blogger_create_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['create_date'], 'permissions': (('can_delete_comment', 'Comment moder'),)},
        ),
    ]
