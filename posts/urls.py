from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='index'),
    path('ajax/newsletter/', views.newsletter, name='newsletter')
]