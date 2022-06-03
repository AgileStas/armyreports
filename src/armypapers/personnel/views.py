from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from personnel.models import Order, Warrior

class OrderDetailView(DetailView):

    model = Order

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class OrderListView(ListView):

    model = Order
    paginate_by = 10

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class WarriorDetailView(DetailView):

    model = Warrior

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class WarriorListView(ListView):

    model = Warrior

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context
