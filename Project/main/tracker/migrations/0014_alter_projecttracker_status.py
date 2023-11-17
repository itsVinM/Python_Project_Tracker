# Generated by Django 4.2.7 on 2023-11-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_projecttracker_sgate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttracker',
            name='status',
            field=models.CharField(blank=True, choices=[('COMPLETED', 'COMPLETED'), ('NOT STARTED', 'NOT STARTED'), ('CANCELED', 'CANCELED'), ('white', 'STARTED'), ('green', 'ON TIME'), ('yellow', 'SLIGHT DELAY')], default='NOT STARTED', max_length=50, null=True),
        ),
    ]
