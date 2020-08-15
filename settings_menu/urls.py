from django.urls import path
from settings_menu import views

app_name = 'settings_menu'

urlpatterns = [
    path('', views.init, name='init'),
]
