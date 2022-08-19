from django.urls import path

from . import views

from personnel.views import OrderDetailView, OrderListView, WarriorDetailView, WarriorListView, WarriorListMilView, WarriorListBloodView, WarriorListWeaponView, WarriorListExerptView, WarriorListContactsView

urlpatterns = [
    #path('<slug:number>/', OrderDetailView.as_view(), name='order-detail'),
    #path('order<int:number>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('warriors/', WarriorListView.as_view(), name='warrior-list'),
    path('warriors_blood/', WarriorListBloodView.as_view(), name='warrior-list-blood'),
    path('weapons/', WarriorListWeaponView.as_view(), name='warrior-list-weapon'),
    path('warrior/<int:pk>', WarriorDetailView.as_view(), name='warrior-detail'),
    path('mil/', WarriorListMilView.as_view(), name='warrior-list-mil'),
    path('exerpt/', WarriorListExerptView.as_view(), name='warrior-list-exerpt'),
    path('contacts/', WarriorListContactsView.as_view(), name='warrior-list-contacts'),
]
