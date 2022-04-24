from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, ListView, UpdateView, DeleteView

from car_cost_tracker.accounts.forms import CreateProfileForm, CreateEditProfileForm
from car_cost_tracker.accounts.models import Profile


class UserRegisterView(CreateView):
    template_name = 'accounts/profile-create.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('login user')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login user')
        return super().dispatch(request, *args, **kwargs)

class UserLoginView(LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('all expense')


    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change-password.html'

class EditProfileView(UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit.html'
    form_class = CreateEditProfileForm
    success_url = reverse_lazy('dashboard')


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile-details.html'
    model = Profile
    context_object_name = 'profile'

    # def get_queryset(self):
    #     user = self.request.user
    #     expense_list = Profile.objects.filter(user=user)   # we give only objects from this user
    #
    #
    #     return expense_list

