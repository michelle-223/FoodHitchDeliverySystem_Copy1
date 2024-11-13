# Generated by Django 5.0.7 on 2024-09-12 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0011_alter_rider_license'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rider',
            options={'verbose_name_plural': 'Riders'},
        ),
        migrations.AddField(
            model_name='rider',
            name='Status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='pending', max_length=10),
        ),
    ]
