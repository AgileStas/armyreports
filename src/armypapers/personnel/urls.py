from django.urls import path

from . import views

from personnel.views import OrderDetailView, OrderListView, WarriorDetailView, WarriorListView, WarriorListMilView, WarriorListBloodView, WarriorListWeaponView, WarriorListExerptView, WeaponsAd14ListView, PositionListView, RankOrderListView, PositionWeaponListView, PositionBirthdaysView, PositionContactsView#, PdfPositionListView

urlpatterns = [
    #path('<slug:number>/', OrderDetailView.as_view(), name='order-detail'),
    #path('order<int:number>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    path('warriors/', WarriorListView.as_view(), name='warrior-list'),
    path('warriors_blood/', WarriorListBloodView.as_view(), name='warrior-list-blood'),
    path('weapons/', WarriorListWeaponView.as_view(), name='warrior-list-weapon'),
    path('weapons_ad14/', WeaponsAd14ListView.as_view(), name='weapons-addendum14'),
    path('warrior/<int:pk>', WarriorDetailView.as_view(), name='warrior-detail'),
    path('mil/', WarriorListMilView.as_view(), name='warrior-list-mil'),
    path('exerpt/', WarriorListExerptView.as_view(), name='warrior-list-exerpt'),
    path('positions/', PositionListView.as_view(), name='position-list'),
    path('ranks/', RankOrderListView.as_view(), name='rank-list'),
    path('position_weapon/', PositionWeaponListView.as_view(), name='position-weapon-list'),
    path('position_weapon_list/', PositionWeaponListView.as_view(template_name='personnel/position_weapon_list1.html'), name='position-weapon-list-1'),
    path('position_weapon_list-2/', PositionWeaponListView.as_view(template_name='personnel/position_weapon_list2.html'), name='position-weapon-list-2'),
    path('warrior_state_changes/', PositionWeaponListView.as_view(template_name='personnel/warrior_state_changes.html'), name='warrior-state-changes'),
    path('position_v/', PositionWeaponListView.as_view(template_name='personnel/position_v.html'), name='position-v'),
    path('profile/', PositionWeaponListView.as_view(template_name='personnel/profile.html'), name='profile'),
    path('report/', PositionWeaponListView.as_view(template_name='personnel/report.html'), name='report'),
    path('medbook/', PositionWeaponListView.as_view(template_name='personnel/medbook.html'), name='medbook'),
    path('birthdays/', PositionBirthdaysView.as_view(), name='birthdays'),
    path('contacts/', PositionContactsView.as_view(), name='contacts'),
    #path('pdf/', PdfPositionListView.as_view(), name='pdf'),
]
