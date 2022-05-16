# Generated by Django 4.0.3 on 2022-04-23 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30)),
                ('horse_power', models.IntegerField()),
                ('cubic', models.FloatField()),
                ('vehicle_condition', models.CharField(choices=[('New', 'New'), ('Second hand', 'Second hand'), ('Third hand', 'Third hand')], max_length=11)),
                ('mileage', models.IntegerField()),
                ('year', models.DateField(blank=True, null=True)),
                ('fuel_type', models.CharField(choices=[('Diesel', 'Diesel'), ('Petrol', 'Petrol'), ('LPG', 'LPG'), ('Petrol and LPG', 'Petrol and LPG'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], max_length=14)),
                ('transmission', models.CharField(choices=[('Automatic gearbox', 'Automatic gearbox'), ('Manual gearbox', 'Manual gearbox'), ('Semi-automatic gearbox', 'Semi-automatic gearbox')], max_length=22)),
                ('photo', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Engine', 'Engine'), ('Transimission', 'Transimission'), ('Interior', 'Interior'), ('Brakes', 'Brakes'), ('Tyres', 'Tyres'), ('Electrical system', 'Electrical system')], max_length=17)),
                ('date_of_purchase', models.DateTimeField(auto_now_add=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car', to='main.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
