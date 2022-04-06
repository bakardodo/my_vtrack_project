
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.

# Create User(then user manager in managers.py) and Profile here
from car_cost_tracker.accounts.managers import CarCostTrackerManager




class CarCostTrackerUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_MAX_LENGTH = 30
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True
    )

    data_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )  # for administration

    USERNAME_FIELD = 'username'  # set USERNAME_FIELD in built-in AbstractBaseUser

    objects = CarCostTrackerManager()

    # User need to be set in settings.py as AUTH_USER_MODEL

class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 40
    LAST_NAME_MAX_LENGTH = 40

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    picture = models.URLField(
        null=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max((len(x) for x, _ in GENDERS)),
        choices=GENDERS,
        null=True,
        blank=True,
    )

    user = models.OneToOneField( # variable 'user' is need to the same way because it is reference with request.'user'
        CarCostTrackerUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
