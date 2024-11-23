# Generated by Django 5.0.7 on 2024-11-22 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0056_alter_delivery_deliverystatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('RiderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='FoodHitchApp.rider')),
            ],
        ),
    ]
