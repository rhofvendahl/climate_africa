from django.urls import path
from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.init, name='init'),
    path('select/', views.select, name='select'),
]
