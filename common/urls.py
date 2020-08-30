from django.urls import path
from common import views

app_name = 'common'

urlpatterns = [
    path('', views.init, name='init'),
    path('welcome/', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('join/', views.join, name='join'),
]
