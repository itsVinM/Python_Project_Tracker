# Generated by Django 4.1.3 on 2023-11-21 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0034_detailskpi_delete_detailsinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projecttracker',
            name='responsible',
            field=models.CharField(blank=True, choices=[('Equipment Development', 'Equipment Development'), ('Equipment Operation', 'Equipment Operation'), ('Not Started', 'Not Started')], max_length=100, null=True),
        ),
    ]
