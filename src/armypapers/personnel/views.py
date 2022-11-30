from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

from personnel.models import Order, Warrior, WarriorWeapon, Position, RankOrder

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

class WeaponsAd14ListView(ListView):

    model = WarriorWeapon

    #template_name = 'warrior_blood'
    template_name = 'personnel/weapons_ad14.html'

    #def get_queryset(self):
    #    return WarriorWeapon.objects.filter(weapon__wtype='Пістолет')

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

class PositionListView(ListView):

    model = Position

    #template_name = 'warrior_blood'
    #template_name = 'personnel/contacts.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class RankOrderListView(ListView):

    model = RankOrder

    template_name = 'personnel/warrior_rank.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class PositionWeaponListView(ListView):

    model = Position

    template_name = 'personnel/position_weapon_list.html'

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class PositionBirthdaysView(ListView):

    model = Position

    template_name = 'personnel/birthdays.html'

    def get_queryset(self):
        #position.position.person.birth_date
        return Position.objects.all().order_by('position__person__birth_date__month', 'position__person__birth_date__day')#.values()

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

class PositionContactsView(ListView):

    model = Warrior

    template_name = 'personnel/contacts.html'

    def get_queryset(self):
        #position.position.person.birth_date
        return Position.objects.all().order_by('position__person__family_name')#.values()

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        return context

#### https://docs.djangoproject.com/en/4.1/howto/outputting-pdf/
###import io
###from django.http import FileResponse
###from reportlab.pdfgen import canvas
###class PdfPositionListView(ListView):
###
###    model = Position
###
###    template_name = 'personnel/position_weapon_list.html'
###
####    def get_context_data(self, **kwargs):
####        context = super().get_context_data(**kwargs)
####        return context
###
###    def render_to_response(self, context, **kwargs):
###        values = Position.objects.all()#.values()
###
###        # Create a file-like buffer to receive PDF data.
###        buffer = io.BytesIO()
###
###        # Create the PDF object, using the buffer as its "file."
###        p = canvas.Canvas(buffer)
###
###        # Draw things on the PDF. Here's where the PDF generation happens.
###        # See the ReportLab documentation for the full list of functionality.
###        #p.drawString(100, 100, "Hello world.")
###        p.drawString(100, 100, values[0].position_fact.person.full_name)
###
###        # Close the PDF object cleanly, and we're done.
###        p.showPage()
###        p.save()
###
###        # FileResponse sets the Content-Disposition header so that browsers
###        # present the option to save the file.
###        buffer.seek(0)
###        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
