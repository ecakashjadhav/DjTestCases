# Generated by Django 4.0.4 on 2022-05-11 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content_type',
            new_name='content',
        ),
    ]
