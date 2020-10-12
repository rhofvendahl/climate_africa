from django.urls import path
from help import views

app_name = 'help'

urlpatterns = [
    path('', views.init, name='init'),
    path('select', views.select, name='select'),
]
