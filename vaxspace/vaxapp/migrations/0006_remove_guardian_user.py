# Generated by Django 4.0 on 2023-12-08 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0005_guardian_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='user',
        ),
    ]