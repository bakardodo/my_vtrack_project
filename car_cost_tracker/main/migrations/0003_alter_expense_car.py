# Generated by Django 4.0.3 on 2022-04-10 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_expense_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.car'),
        ),
    ]
