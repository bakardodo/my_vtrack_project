from django import forms
from django.forms import TextInput

from car_cost_tracker.main.models import Expense, Car


class CreateExpenseForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=None)  # we make choicefield for all car objects

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['car'].queryset = Car.objects.all()  # we make queryset and fill it with all car objects

    def save(self, commit=True):
        expense = super().save(commit=False)
        expense.user = self.user
        if commit:
            expense.save()
        return expense

    class Meta:
        model = Expense
        fields = ('part', 'type', 'description', 'car')
        widgets = {
                'part': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter part name',
                    }
                ),
        }

class CreateVehicleForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        vehicle = super().save(commit=False)

        vehicle.user = self.user
        if commit:
            vehicle.save()
        return vehicle

    class Meta:
        model = Car
        fields = ('make', 'horse_power', 'cubic', 'vehicle_condition', 'mileage', 'year', 'fuel_type', 'transmission', 'photo')
