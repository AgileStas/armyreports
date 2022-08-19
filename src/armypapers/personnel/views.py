from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from personnel.models import Order, Warrior, WarriorWeapon

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

class WarriorListMilView(ListView):

    model = Warrior

    #template_name = 'mil'
    template_name = 'personnel/warrior_mil_list.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class WarriorListBloodView(ListView):

    model = Warrior

    #template_name = 'warrior_blood'
    template_name = 'personnel/warrior_blood_list.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class WarriorListWeaponView(ListView):

    model = WarriorWeapon

    #template_name = 'warrior_blood'
    template_name = 'personnel/weapons.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class WarriorListExerptView(ListView):

    model = Warrior

    #template_name = 'warrior_blood'
    template_name = 'personnel/exerpt.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class WarriorListContactsView(ListView):

    model = Warrior

    #template_name = 'warrior_blood'
    template_name = 'personnel/contacts.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context
