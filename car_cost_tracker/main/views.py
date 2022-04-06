from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView

from car_cost_tracker.accounts.models import CarCostTrackerUser
from car_cost_tracker.main.forms import CreateExpenseForm


class HomeView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_nav'] = True
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)

class DashboardView(TemplateView):
    template_name = 'main/dashboard.html'



class CreateCostView(CreateView):
    template_name = 'main/create-cost.html'
    form_class = CreateExpenseForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class CreateExpenseDetailView(DetailView):
    model = Expense