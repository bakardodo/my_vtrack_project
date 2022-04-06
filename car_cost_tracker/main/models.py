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