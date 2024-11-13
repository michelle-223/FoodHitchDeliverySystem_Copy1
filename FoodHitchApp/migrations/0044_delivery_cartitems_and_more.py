# Generated by Django 5.0.7 on 2024-10-06 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0043_remove_delivery_foodid_remove_order_foodid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='CartItems',
            field=models.ManyToManyField(blank=True, to='FoodHitchApp.cartitem'),
        ),
        migrations.AlterUniqueTogether(
            name='deliveryitem',
            unique_together={('Delivery', 'FoodID')},
        ),
    ]
