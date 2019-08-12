from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-home'),
    path('new/home/', create_neighbourhood, name='createhood'),
    path('join/(?P<neigh_id>\d+)', join_neighbourhood, name='join'),
    path('leave/(?P<neigh_id>\d+)', leave_neighbourhood, name='left'),
    path('delete/(?P<neigh_id>\d+)', delete_neighbourhood, name='deletehood'),
    path('edit/(?P<neigh_id>\d+)', edit_neighbourhood, name='edithood'),
    path('hoods/', neighbourhoods, name='hoods'),
]
