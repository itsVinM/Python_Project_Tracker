# Generated by Django 4.2.7 on 2023-11-20 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0028_alter_projecttracker_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttracker',
            name='currentForecast',
        ),
        migrations.RemoveField(
            model_name='projecttracker',
            name='lastUpdate',
        ),
    ]
