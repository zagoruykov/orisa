# Generated by Django 4.1.7 on 2023-03-11 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_vehicle_price'),
        ('trips', '0011_alter_trip_adults_alter_trip_free_alter_trip_kids_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='guide',
            new_name='guides',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='vehicle',
        ),
        migrations.CreateModel(
            name='VehiclesTrips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('date', models.DateTimeField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='vehicle',
            field=models.ManyToManyField(through='trips.VehiclesTrips', to='staff.vehicle'),
        ),
    ]
