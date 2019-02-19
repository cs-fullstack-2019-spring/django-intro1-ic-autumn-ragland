from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('languages/', views.lang, name='lang'),
    path('system/', views.system, name='system'),
    path('terminal/', views.terminal, name='terminal'),
]
