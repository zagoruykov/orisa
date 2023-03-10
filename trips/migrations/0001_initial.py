# Generated by Django 4.1.7 on 2023-02-27 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('staff', '0001_initial'),
        ('sights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='days', to='sights.sight')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('paid', models.PositiveSmallIntegerField()),
                ('free', models.PositiveSmallIntegerField()),
                ('commission', models.DecimalField(decimal_places=2, max_digits=6)),
                ('profit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='clients.client')),
                ('days', models.ManyToManyField(through='trips.Day', to='sights.sight')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='staff.guide')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='staff.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='day',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip'),
        ),
    ]
