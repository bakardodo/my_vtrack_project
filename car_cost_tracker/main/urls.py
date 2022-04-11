from django.urls import path

from car_cost_tracker.main.views import HomeView, CreateCostView, CreateCostDetailView, DashboardView, CreateCarView, \
    CreateCarDetailView

urlpatterns = (
    path('', HomeView.as_view(), name='index view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/cost/', CreateCostView.as_view(), name='create cost'),
    # path('detail/cost/', CreateCostDetailView.as_view(), name='detail cost'),
    path('create/car/', CreateCarView.as_view(), name='create car'),
    path('detail/car/', CreateCarDetailView.as_view(), name='detail car'),
)

