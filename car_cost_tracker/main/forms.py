from django import forms
from django.forms import TextInput




class CreateExpenseForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        expense = super().save(commit=False)

        expense.user = self.user
        if commit:
            expense.save()
        return expense

    class Meta:
        fields = ('part', 'type', 'description',)
        widgets = {
                'part': forms.TextInput(
                    attrs={
                        'placeholder': 'Enter part name',
                    }
                ),
                'description': forms.TextInput(
                    attrs={
                        'background-color':'red'
                    }
                ),

            }


