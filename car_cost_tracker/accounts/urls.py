from django.urls import path

from car_cost_tracker.accounts.views import UserLoginView, ChangePasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('edit/password/', ChangePasswordView.as_view(), name='change password',)
    # path('', EditProfileView.as_view(), name='edit profile'),
)