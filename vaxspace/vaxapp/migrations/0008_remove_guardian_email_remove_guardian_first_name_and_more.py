# Generated by Django 4.0 on 2023-12-08 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('vaxapp', '0007_alter_register_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guardian',
            name='email',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='group',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='password',
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='username',
        ),
        migrations.AddField(
            model_name='guardian',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
