from django.urls import path
from compose import views

app_name = 'compose'

urlpatterns = [
    path('', views.init, name='init'),
    path('new/', views.new, name='new'),
]
