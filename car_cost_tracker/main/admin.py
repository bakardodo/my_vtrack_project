from django.contrib import admin

# Register your models here.
from car_cost_tracker.main.models import Expense, Car


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass