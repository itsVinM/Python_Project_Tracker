# Generated by Django 4.2.7 on 2023-11-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0017_remove_projecttracker_sgate_date_infoproject_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoproject',
            name='qualityEng',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infoproject',
            name='support',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='infoproject',
            name='testEng',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
