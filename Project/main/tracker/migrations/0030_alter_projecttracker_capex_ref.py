# Generated by Django 4.2.7 on 2023-11-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0029_remove_projecttracker_currentforecast_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttracker',
            name='CapEx_Ref',
            field=models.CharField(default=0, max_length=250),
        ),
    ]