# Generated by Django 4.1.7 on 2023-02-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0005_alter_sight_address_alter_sight_contact_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='kids_price',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
