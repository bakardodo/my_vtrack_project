from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class UserRegisterView(CreateView):
    pass

class UserLoginView(LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index view')


    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()

class ChangePasswordView(PasswordChangeView):
    pass

class EditProfileView(TemplateView):
    pass

class ProfileDetailView:
    pass
