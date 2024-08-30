from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_plus, name='home'),
    path('home_plus/', views.home_plus, name='home_plus'),
    path('news/', views.news, name='news'),
]