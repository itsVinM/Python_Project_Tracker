# Generated by Django 4.2.7 on 2023-11-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0018_infoproject_qualityeng_infoproject_support_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoproject',
            name='currentForecast',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='infoproject',
            name='lastUpdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
