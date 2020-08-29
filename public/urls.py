from django.urls import path
from public import views

app_name = 'public'

urlpatterns = [
    # path('', views.init, name='init'),
    path('login/', views.login, name='login'),
]
