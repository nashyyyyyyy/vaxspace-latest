# Generated by Django 4.0 on 2023-12-08 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vaxapp', '0002_guardian'),
    ]

    operations = [
        migrations.AddField(
            model_name='guardian',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vaxapp.barangay'),
        ),
    ]
