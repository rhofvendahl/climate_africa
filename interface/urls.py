from django.urls import path
from interface import views

app_name = 'interface'

urlpatterns = [
    path('', views.test, name='test'),
]
