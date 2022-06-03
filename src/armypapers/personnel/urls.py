from django.urls import path

from . import views

from personnel.views import OrderDetailView, OrderListView, WarriorDetailView, WarriorListView

urlpatterns = [
    #path('<slug:number>/', OrderDetailView.as_view(), name='order-detail'),
    #path('order<int:number>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('warriors/', WarriorListView.as_view(), name='warrior-list'),
    path('warrior/<int:pk>', WarriorDetailView.as_view(), name='warrior-detail'),
]
