# Generated by Django 4.2.7 on 2023-11-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0032_detailsinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttracker',
            name='latesBase_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projecttracker',
            name='latesForecast_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
