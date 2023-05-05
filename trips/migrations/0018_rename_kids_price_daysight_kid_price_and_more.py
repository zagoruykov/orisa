# Generated by Django 4.1.7 on 2023-03-14 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0017_alter_daysight_extra'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daysight',
            old_name='kids_price',
            new_name='kid_price',
        ),
        migrations.RemoveField(
            model_name='daysight',
            name='extra',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='adults',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='free',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='kids',
        ),
        migrations.AddField(
            model_name='daysight',
            name='adults_quantity',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='daysight',
            name='kids_quantity',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guidetrips',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclestrips',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
