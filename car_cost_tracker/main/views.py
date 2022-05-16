from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, DeleteView, UpdateView

from car_cost_tracker.accounts.models import CarCostTrackerUser
from car_cost_tracker.main.forms import CreateExpenseForm, CreateVehicleForm, CreateEditExpenseForm, CreateCarEditForm, \
    CreateFeedbackForm
from car_cost_tracker.main.models import Expense, Car


class HomeView(TemplateView):
    template_name = 'main/home-page-login-and-register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(ListView):
    template_name = 'main/dashboard.html'
    model = Expense
    context_object_name = 'expenses'

    def get_queryset(self):
        user = self.request.user
        expense_list = Expense.objects.filter(user=user)   # we give only objects from this user

        return expense_list

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        all_obj = Expense.objects.filter(user=user)
        expenses = sum([x.price for x in all_obj if x.price])
        context['all_expenses'] = expenses
        return context

class CreateCostView(CreateView):
    template_name = 'main/create-cost.html'
    form_class = CreateExpenseForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


# class CreateCostDetailView(ListView):
#     model = Expense
#     template_name = 'main/dashboard.html'
#     context_object_name = 'expenses'
#
#     def get_queryset(self):
#         user = self.request.user
#         expense_list = Expense.objects.filter(user=user)   # we give only objects from this user
#
#
#         return expense_list

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context


class CreateCarView(CreateView):
    template_name = 'main/create-car.html'
    form_class = CreateVehicleForm
    success_url = reverse_lazy('detail car')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class CreateCarDetailView(ListView):
    model = Car
    template_name = 'main/details-car.html'
    context_object_name = 'cars'


    def get_queryset(self):
        user = self.request.user
        car_list = Car.objects.filter(user=user)

        return car_list



    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context

class DeleteExpenseView(DeleteView):
    model = Expense
    template_name = 'main/delete-cost.html'
    # form_class = DeteleExpenseForm
    # context_object_name = 'expense'
    success_url = reverse_lazy('dashboard')


class EditExpenseView(UpdateView):
    model = Expense
    template_name = 'main/edit-cost.html'
    form_class = CreateEditExpenseForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class EditCarView(UpdateView):
    model = Car
    template_name = 'main/edit-car.html'
    form_class = CreateCarEditForm
    success_url = reverse_lazy('dashboard')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

class DeleteCarView(DeleteView):
    model = Car
    template_name = 'main/delete-car.html'
    # form_class = DeteleExpenseForm
    # context_object_name = 'expense'
    success_url = reverse_lazy('dashboard')

class CreateFeedbackView(CreateView):
    form_class = CreateFeedbackForm
    template_name = 'main/feedback.html'
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CreateListAllExpenseView(ListView):
    model = Expense
    template_name = 'main/all_expense.html'
    context_object_name = 'all_expense_of_database'