from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('new/home/', views.create_neighbourhood, name='createhood'),
    path('join/(?P<neigh_id>\d+)', views.join_neighbourhood, name='join'),
    path('leave/(?P<neigh_id>\d+)', views.leave_neighbourhood, name='left'),
    path('delete/(?P<neigh_id>\d+)', views.delete_neighbourhood, name='deletehood'),
    path('hoods/', views.neighbourhoods, name='hoods'),
]
