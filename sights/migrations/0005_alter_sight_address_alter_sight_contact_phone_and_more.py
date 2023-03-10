# Generated by Django 4.1.7 on 2023-02-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sights', '0004_sight_shared'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sight',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='contact_phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='sight',
            name='tags',
            field=models.ManyToManyField(null=True, related_name='sights', to='sights.tag'),
        ),
    ]
