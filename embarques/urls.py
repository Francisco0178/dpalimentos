from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='embarques-home'),
    path('about/', views.about, name='embarques-about'),
    path('perfil', views.perfil, name='embarques-perfil'),
    path('historial', views.historial, name='embarques-historial'),
    path('embarque/', views.embarque, name='embarques-embarque'),
    path('runCode/', views.runCode, name='runCode'),
]