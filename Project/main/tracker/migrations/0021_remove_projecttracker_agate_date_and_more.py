# Generated by Django 4.2.7 on 2023-11-16 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0020_remove_infoproject_requested_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttracker',
            name='agate_date',
        ),
        migrations.RemoveField(
            model_name='projecttracker',
            name='rgate_date',
        ),
        migrations.RemoveField(
            model_name='projecttracker',
            name='vgate_date',
        ),
        migrations.AddField(
            model_name='infoproject',
            name='agate_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='infoproject',
            name='rgate_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='infoproject',
            name='vgate_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
