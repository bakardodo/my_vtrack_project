from django import forms
from django.forms import TextInput

from car_cost_tracker.main.models import Expense, Car, Feedback


# class DeteleExpenseForm(forms.ModelForm):
#
#     def save(self, commit=True):
#         self.instance.delete()
#         return self.instance
#
#     class Meta:
#         model = Expense
#         fields = ()
class CreateEditExpenseForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['car'].queryset = Car.objects.filter(user=user)

    class Meta:
        model = Expense
        exclude = ('user', 'photo',)

class CreateExpenseForm(forms.ModelForm):
    car = forms.ModelChoiceField(queryset=None)  # we make choicefield for all car objects

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['car'].queryset = Car.objects.filter(user=user)  # we make queryset and fill it with all car objects

    def save(self, commit=True):
        expense = super().save(commit=False)
        expense.user = self.user
        if commit:
            expense.save()
        return expense

    class Meta:
        model = Expense
        fields = ('part', 'type', 'description', 'price', 'car')
        widgets = {
                'part': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter part name',
                    }
                ),
                'description': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter your description',
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

class CreateCarEditForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ('user',)

class CreateFeedbackForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        feedback = super().save(commit=False)

        feedback.user = self.user
        if commit:
            feedback.save()
        return feedback

    class Meta:
        model = Feedback
        fields = ('requester', 'to', 'message')
        widgets = {
            'requester': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your username',
                }
            ),
            'to': forms.TextInput(
                attrs={
                    'placeholder': 'VTRACK support',
                }
            ),
            'message': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your message',
                }
            ),

        }
