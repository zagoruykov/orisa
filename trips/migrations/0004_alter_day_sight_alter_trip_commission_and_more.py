# Generated by Django 4.1.7 on 2023-02-27 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0003_alter_price_adult_price_alter_price_kids_price'),
        ('trips', '0003_rename_paid_trip_adults_trip_kids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='sight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sights.sight'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='commission',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='trip',
            name='days',
            field=models.ManyToManyField(related_name='days', through='trips.Day', to='sights.sight'),
        ),
        migrations.AlterField(
            model_name='trip',
            name='profit',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]