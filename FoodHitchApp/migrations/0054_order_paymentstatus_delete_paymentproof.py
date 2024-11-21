# Generated by Django 5.0.7 on 2024-11-20 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0053_pendingorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='PaymentStatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending', max_length=12),
        ),
        migrations.DeleteModel(
            name='PaymentProof',
        ),
    ]
