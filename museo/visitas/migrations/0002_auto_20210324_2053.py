# Generated by Django 3.1.7 on 2021-03-24 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='timestamp_in',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='visita',
            name='timestamp_out',
            field=models.DateTimeField(blank=True),
        ),
    ]
