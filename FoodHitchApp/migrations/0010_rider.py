# Generated by Django 5.0.7 on 2024-09-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodHitchApp', '0009_alter_customer_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('RiderID', models.BigAutoField(primary_key=True, serialize=False)),
                ('FullName', models.CharField(max_length=100)),
                ('Username', models.CharField(default='default_rider_username', max_length=100, unique=True)),
                ('Email', models.EmailField(default='rider@example.com', max_length=254)),
                ('Phone', models.CharField(max_length=15)),
                ('ProfilePicture', models.ImageField(blank=True, null=True, upload_to='rider_pictures')),
                ('License', models.CharField(max_length=50)),
                ('PlateNumber', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Rider',
            },
        ),
    ]
