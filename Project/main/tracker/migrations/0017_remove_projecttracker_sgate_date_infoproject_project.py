# Generated by Django 4.2.7 on 2023-11-16 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0016_projecttracker_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttracker',
            name='sgate_date',
        ),
        migrations.AddField(
            model_name='infoproject',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.projecttracker'),
        ),
    ]
