# Generated by Django 5.0.7 on 2024-11-20 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0052_remove_order_paymentstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=255)),
                ('Subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('DeliveryFee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TotalPayableAmount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PaymentOption', models.CharField(max_length=50)),
                ('OrderDetails', models.TextField()),
                ('CreatedAt', models.DateTimeField(auto_now_add=True)),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodHitchApp.customer')),
                ('RestaurantID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FoodHitchApp.restaurant')),
            ],
        ),
    ]
