from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from car_cost_tracker.accounts.views import UserLoginView, ChangePasswordView, UserRegisterView, ProfileDetailView, \
    EditProfileView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('edit/password/', ChangePasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),
    path('create/profile/', UserRegisterView.as_view(), name='create profile'),
    # path('', EditProfileView.as_view(), name='edit profile'),
    path('<int:pk>/', ProfileDetailView.as_view(), name='profile details'),
    path('edit/profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
)