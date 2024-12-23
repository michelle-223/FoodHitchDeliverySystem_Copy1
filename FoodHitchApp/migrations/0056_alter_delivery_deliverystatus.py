# Generated by Django 5.0.7 on 2024-11-21 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0055_alter_delivery_deliverystatus_delete_pendingorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='DeliveryStatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('On Transit', 'On Transit'), ('Delivered', 'Delivered'), ('Received', 'Received'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]
