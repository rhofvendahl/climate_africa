from django.urls import path
from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.init, name='init'),
    path('select/', views.select, name='select'),
    path('change-info/', views.change_info, name='change_info'),
    path('change-password/', views.change_password, name='change_password'),
]
