# Generated by Django 4.2.10 on 2024-02-16 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0002_measurement_instant'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='type',
            field=models.IntegerField(null=True),
        ),
    ]
