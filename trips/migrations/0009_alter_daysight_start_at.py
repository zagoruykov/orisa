# Generated by Django 4.1.7 on 2023-03-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0008_alter_daysight_options_daysight_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daysight',
            name='start_at',
            field=models.TimeField(blank=True),
        ),
    ]
