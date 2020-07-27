from django.urls import path
from posts import views

app_name = 'interface'

urlpatterns = [
    path('', views.test, name='test'),
]
