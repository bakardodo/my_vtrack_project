from django.contrib.auth import get_user_model
from django.db import models
# Create your models here.

UserModel = get_user_model()

class Expense(models.Model):
    ENGINE = 'Engine'
    TRANSMISSION = 'Transimission'
    INTERIOR = 'Interior'
    BRAKES = 'Brakes'
    TYRES = 'Tyres'
    ELECTRICAL_SYSTEM = 'Electrical system'


    TYPES = [(x, x) for x in (ENGINE, TRANSMISSION, INTERIOR, BRAKES, TYRES, ELECTRICAL_SYSTEM)]

    PART_NAME_MAX_LENGTH = 50

    part = models.CharField(
        max_length=PART_NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    date_of_purchase = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )

    photo = models.ImageField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE,
    )
    my_cars = [('Car', car), ('Car', car)]
    your_cars = models.CharField(
        max_length=50,
        choices=my_cars,
    )

    def __str__(self):
        return self.part

class Car(models.Model):
    AUTOMATIC_GEARBOX = 'Automatic gearbox'
    MANUAL_GEARBOX = 'Manual gearbox'
    SEMI_AUTOMATIC_GEARBOX = 'Semi-automatic gearbox'

    GEARBOX_TYPE = [(x, x) for x in (AUTOMATIC_GEARBOX, MANUAL_GEARBOX, SEMI_AUTOMATIC_GEARBOX)]

    DIESEL = 'Diesel'
    PETROL = 'Petrol'
    LPG = 'LPG'
    PETROL_AND_LPG = 'Petrol and LPG'
    HYBRID = 'Hybrid'
    ELECTRIC = 'Electric'

    FUEL_TYPE = [(x, x) for x in (DIESEL, PETROL, LPG, PETROL_AND_LPG, HYBRID, ELECTRIC)]

    NEW = 'New'
    SECOND_HAND = 'Second hand'
    THIRD_HAND = 'Third hand'

    VEHICLE_CONDITION_TYPE = [(x, x) for x in (NEW, SECOND_HAND, THIRD_HAND)]

    MODEL_MAX_LENGTH = 30

    make = models.CharField(
        max_length=MODEL_MAX_LENGTH,
    )

    horse_power = models.IntegerField()

    cubic = models.FloatField()

    vehicle_condition = models.CharField(
        max_length=max(len(x) for (x, _) in VEHICLE_CONDITION_TYPE),
        choices=VEHICLE_CONDITION_TYPE,
    )

    mileage = models.IntegerField()

    year = models.DateField(
        null=True,
        blank=True,
    )

    fuel_type = models.CharField(
        max_length=max(len(x) for (x, _) in FUEL_TYPE),
        choices=FUEL_TYPE
    )

    transmission = models.CharField(
        max_length=max(len(x) for (x, _) in GEARBOX_TYPE),
        choices=GEARBOX_TYPE,
    )

    photo = models.URLField(
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.make





