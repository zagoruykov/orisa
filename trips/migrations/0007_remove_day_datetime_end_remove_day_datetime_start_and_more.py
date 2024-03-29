# Generated by Django 4.1.7 on 2023-03-06 09:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0009_sight_timing'),
        ('trips', '0006_guidetrips_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='datetime_end',
        ),
        migrations.RemoveField(
            model_name='day',
            name='datetime_start',
        ),
        migrations.RemoveField(
            model_name='day',
            name='sight',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='days',
        ),
        migrations.AddField(
            model_name='day',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='day',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='trips.trip'),
        ),
        migrations.CreateModel(
            name='DaySight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_at', models.TimeField()),
                ('end_at', models.TimeField()),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.day')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sights.sight')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='sights',
            field=models.ManyToManyField(through='trips.DaySight', to='sights.sight'),
        ),
    ]
