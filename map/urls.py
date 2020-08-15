from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('', views.init, name='init'),
    path('posts/', views.posts, name='posts'),
]
