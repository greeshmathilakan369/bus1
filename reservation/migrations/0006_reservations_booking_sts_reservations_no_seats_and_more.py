# Generated by Django 4.1.3 on 2023-03-23 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0005_bus_list_available_seats_bus_list_distance_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='booking_sts',
            field=models.CharField(choices=[('BOOKED', 'BOOKED'), ('CANCELLD', 'CANCELLD')], default='BOOKED', max_length=20),
        ),
        migrations.AddField(
            model_name='reservations',
            name='no_seats',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reservations',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='reservations',
            unique_together={('custid', 'busid')},
        ),
    ]
