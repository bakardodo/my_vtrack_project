from django.urls import path

from car_cost_tracker.main.views import HomeView, CreateCostView, DashboardView, CreateCarView, \
    CreateCarDetailView, DeleteExpenseView, EditExpenseView, EditCarView, DeleteCarView

urlpatterns = (
    path('', HomeView.as_view(), name='index view'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/cost/', CreateCostView.as_view(), name='create cost'),
    # path('detail/cost/<int:pk>/', CreateCostDetailView.as_view(), name='detail cost'),
    path('create/car/', CreateCarView.as_view(), name='create car'),
    path('detail/car/', CreateCarDetailView.as_view(), name='detail car'),
    path('delete/expense/<int:pk>/', DeleteExpenseView.as_view(), name='delete expense'),
    path('edit/expense/<int:pk>/', EditExpenseView.as_view(), name='edit expense'),
    path('edit/car/<int:pk>/', EditCarView.as_view(), name='edit car'),
    path('delete/car/<int:pk>/', DeleteCarView.as_view(), name='delete car'),
)

