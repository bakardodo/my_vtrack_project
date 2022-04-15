from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from car_cost_tracker.accounts.models import Profile


class CreateProfileForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    picture = forms.URLField()
    date_of_birth = forms.DateField()
    email = forms.EmailField()
    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )


    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'gender','date_of_birth']


class CreateEditProfileForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user


    class Meta:
        model = Profile
        exclude = ('user',)