from django.contrib import admin

# Register your models here.
from car_cost_tracker.accounts.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass