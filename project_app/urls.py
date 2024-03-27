from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='Главная'),
    path('about/', views.about_me, name='О себе')
]
