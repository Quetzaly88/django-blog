# Generated by Django 4.2.16 on 2024-11-01 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_comment_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='challenge',
        ),
    ]
