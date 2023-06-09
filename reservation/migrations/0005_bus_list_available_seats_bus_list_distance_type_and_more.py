# Generated by Django 4.1.3 on 2023-03-23 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_remove_bus_list_bid_reservations'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus_list',
            name='available_seats',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='bus_list',
            name='distance_type',
            field=models.CharField(choices=[('short', 'short'), ('long', 'long'), ('medium', 'medium')], default='short', max_length=20),
        ),
        migrations.AddField(
            model_name='bus_list',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bus_list',
            name='total_seats',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterUniqueTogether(
            name='bus_list',
            unique_together={('distance_type',)},
        ),
    ]
