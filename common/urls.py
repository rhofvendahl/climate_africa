from django.urls import path
from common import views

app_name = 'common'

urlpatterns = [
    path('', views.init, name='init'),
    path('login/', views.login, name='login')
]
