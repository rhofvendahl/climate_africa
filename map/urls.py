from django.urls import path
from map import views

app_name = 'map'

urlpatterns = [
    path('', views.init, name='init'),
    path('map-test/', views.map_test, name='map_test'),
    path('alerts/', views.alerts, name='alerts'),
    path('posts/', views.posts, name='posts'),
]
