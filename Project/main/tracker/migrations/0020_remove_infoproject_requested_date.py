# Generated by Django 4.2.7 on 2023-11-16 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0019_infoproject_currentforecast_infoproject_lastupdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoproject',
            name='requested_date',
        ),
    ]
